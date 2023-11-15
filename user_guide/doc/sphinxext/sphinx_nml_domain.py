# -*- coding: utf-8 -*-
"""
    Fortran namelist domain
"""

import re

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.docfields import Field


class MemberDirective(ObjectDescription):
    """
    Description of a Fortran namelist member object (like a Python function).
    """
    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
    }

    doc_field_types = [
        Field('type', label=_('Type'), has_arg=False,  names=('type')),
        Field('permitted', label=_('Permitted'), has_arg=False, names=('permitted')),
        Field('default', label=_('Default'), has_arg=False, names=('default')),
    ]

    def get_signature_prefix(self, sig):
        """
        May return a prefix to put before the object name in the signature.
        """
        return ''

    def needs_arglist(self):
        """
        May return true if an empty argument list is to be generated even if
        the document contains none.
        """
        return False

    def handle_signature(self, sig, signode):
        """
        Transform a member signature into RST nodes.
        Returns fully qualified name of the thing.
        """
        if sig is None:
            raise ValueError

        # The signature is just the member name
        name = sig

        # Determine namelist name (if applicable), as well as full name
        nmlname = self.options.get('namelist', self.env.temp_data.get('nml:namelist'))
        
        fullname = nmlname + '::' + name

        signode['namelist'] = nmlname
        signode['fullname'] = fullname

        if self.env.config.add_module_names:
            nodetext = nmlname + '::'
            signode += addnodes.desc_addname(nodetext, nodetext)

        signode += addnodes.desc_name(name, name)
        return fullname

    def add_target_and_index(self, name, sig, signode):
        nmlname = self.options.get('namelist', self.env.temp_data.get('nml:namelist'))
        
        prefix = nmlname and nmlname + '::' or ''
        
        fullname = name if '::' in name else nmlname + '::' + name
        
        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['nml']['objects']
            if fullname in objects:
                self.env.warn(
                    self.env.docname,
                    'duplicate object description of %s, ' % fullname +
                    'other instance in ' +
                    self.env.doc2path(objects[fullname][0]),
                    self.lineno)
            objects[fullname] = (self.env.docname, self.objtype)

        # For the index text, strip the namelist name from the fully qualified name
        indextext = _('%s (in namelist %s)') % (name.split('::')[1] if '::' in name else name, nmlname)
        
        if indextext:
            self.indexnode['entries'].append(('single', indextext, fullname, fullname, None))
            
            
class NamelistDirective(Directive):
    """
    Directive to start a new Fortran namelist.
    Namelists are like Python modules - they are invisible but add context to namelist members
    """
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'synopsis': lambda x: x,
        'noindex': directives.flag,
        'deprecated': directives.flag,
    }

    def run(self):
        env = self.state.document.settings.env
        nmlname = self.arguments[0].strip()
        noindex = 'noindex' in self.options
        env.temp_data['nml:namelist'] = nmlname
        env.domaindata['nml']['namelists'][nmlname] = (
            env.docname, self.options.get('synopsis', ''),
            'deprecated' in self.options)

        targetnode = nodes.target('', '', ids=['namelist-' + nmlname], ismod=True)
        self.state.document.note_explicit_target(targetnode)
        ret = [targetnode]

        # the synopsis isn't printed; in fact, it is only used in the
        # modindex currently
        if not noindex:
            indextext = _('%s (namelist)') % nmlname
            inode = addnodes.index(entries=[('single', indextext, 'namelist-' + nmlname, nmlname, None)])
            ret.append(inode)
        
        return ret
    

class NamelistMemberGroupDirective(BaseAdmonition):
    """
    An admonition type construct for namelist members that form a logical group
    Adds no extra context - for semantic purposes in ReST markup only
    """
    required_arguments = 1
    node_class = nodes.admonition


class NamelistXRefRole(XRefRole):
    """
    Provides cross reference links for namelists
    """
    def process_link(self, env, refnode, has_explicit_title, title, target):
        # The target is a namelist, regardless of whether it has been defined yet
        refnode['nml:namelist'] = target
        
        # If an explicit title is not given, just use the member name, not the namelist name
        if not has_explicit_title:
            title = target
        
        return title, target
    

class NamelistMemberXRefRole(XRefRole):
    """
    Provides cross reference links for namelist members
    """
    def process_link(self, env, refnode, has_explicit_title, title, target):        
        # If the target contains a separator, then it is a member target
        if '::' in target:
            # Extract the target namelist name, leave the target unchanged
            target_nml, _ = target.split('::')
        # If the target does not contain a separator, interpret it as a member reference in the current namelist context
        else:
            target_nml = env.temp_data.get('nml:namelist')
            # If there was no target nml (i.e. we are not in a namelist scope...) then leave the target untouched
            # It will be rendered as an unresolved link
            target = target_nml + '::' + target if target_nml else target
            
        refnode['nml:namelist'] = target_nml
        
        # If an explicit title is not given, just use the member name, not the namelist name
        if not has_explicit_title:
            title = target.split('::')[1] if '::' in target else target
        
        return title, target


class NamelistIndex(Index):
    """
    Index subclass to provide the Fortran namelist index.
    """

    name = 'modindex'
    localname = _('Fortran Namelist Index')
    shortname = _('namelists')

    def generate(self, docnames = None):
        content = {}
        # list of prefixes to ignore
        ignores = self.domain.env.config['modindex_common_prefix']
        ignores = sorted(ignores, key=len, reverse=True)
        # list of all modules, sorted by module name
        modules = sorted(self.domain.data['namelists'].items(), key=lambda x: x[0].lower())
        # sort out collapsable modules
        prev_modname = ''
        num_toplevels = 0
        for modname, (docname, synopsis, deprecated) in modules:
            if docnames and docname not in docnames:
                continue

            for ignore in ignores:
                if modname.startswith(ignore):
                    modname = modname[len(ignore):]
                    stripped = ignore
                    break
            else:
                stripped = ''

            # we stripped the whole module name?
            if not modname:
                modname, stripped = stripped, ''

            entries = content.setdefault(modname[0].lower(), [])

            package = modname.split('::')[0]
            if package != modname:
                # it's a submodule
                if prev_modname == package:
                    # first submodule - make parent a group head
                    entries[-1][1] = 1
                elif not prev_modname.startswith(package):
                    # submodule without parent in list, add dummy entry
                    entries.append([stripped + package, 1, '', '', '', '', ''])
                subtype = 2
            else:
                num_toplevels += 1
                subtype = 0

            qualifier = deprecated and _('Deprecated') or ''
            entries.append([stripped + modname, subtype, docname,
                            'namelist-' + stripped + modname, '',
                            qualifier, synopsis])
            prev_modname = modname

        # apply heuristics when to collapse modindex at page load:
        # only collapse if number of toplevel modules is larger than
        # number of submodules
        collapse = len(modules) - num_toplevels < num_toplevels

        # sort by first letter
        content = sorted(content.items())

        return content, collapse


class NamelistDomain(Domain):
    """Fortran namelist domain."""
    
    name = 'nml'
    
    label = 'Fortran namelist'
    
    object_types = {
        'namelist': ObjType(_('namelist'), 'lst', 'obj'),
        'member': ObjType(_('member'), 'mem', 'obj')
    }

    directives = {
        'namelist': NamelistDirective,
        'group' : NamelistMemberGroupDirective,
        'member': MemberDirective
    }

    roles = {
        'lst': NamelistXRefRole(),
        'mem': NamelistMemberXRefRole()
    }

    initial_data = {
        'objects': {},  # fullname -> docname, objtype
        'namelists': {},  # namespace -> docname, synopsis
    }
    
    indices = [
        NamelistIndex,
    ]

    def clear_doc(self, docname):
        for fullname, (fn, _) in list(self.data['objects'].items()):
            if fn == docname:
                del self.data['objects'][fullname]
                
        for nml, (fn, _, _) in list(self.data['namelists'].items()):
            if fn == docname:
                del self.data['namelists'][nml]

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        if (typ == 'lst' or typ == 'obj' and target in self.data['namelists']):
            docname, synopsis, deprecated = self.data['namelists'].get(target, ('', '', ''))
            
            if not docname:
                return None
            else:
                title = '%s%s' % (synopsis, (deprecated and ' (deprecated)' or ''))
                return make_refnode(builder, fromdocname, docname, 'namelist-' + target, contnode, title)
        else:
            nmlname = node.get('nml:namelist')
            searchorder = node.hasattr('refspecific') and 1 or 0
            name, obj = self.find_obj(env, nmlname, target, typ, searchorder)
            
            if not obj:
                return None
            else:
                return make_refnode(builder, fromdocname, obj[0], name, contnode, name)

    def find_obj(self, env, nmlname, name, type, searchorder=0):
        """
        Find a namelist object for "name", perhaps using the given namelist.
        """
        if not name:
            return None, None

        objects = self.data['objects']
        
        newname = None
        if searchorder == 1:
            if nmlname and nmlname + '::' + name in objects:
                newname = nmlname + '::' + name
            elif name in objects:
                newname = name
        else:
            if name in objects:
                newname = name
            elif nmlname and nmlname + '::' + name in objects:
                newname = nmlname + '::' + name

        if newname is None:
            return None, None
        
        return newname, objects[newname]

    def get_objects(self):
        for nml, info in self.data['namelists'].items():
            yield (nml, nml, 'namelist', info[0], 'namelist-' + nml, 0)
        
        for refname, (docname, type) in self.data['objects'].items():
            yield (refname, refname, type, docname, refname, 1)


def setup(app):
    app.add_domain(NamelistDomain)
