# External libs
from lxml.builder import E
import lxml.etree

# Local libs
from raw_txt import RawTextRfcWriter

# HTML Specific Defaults that are not provided in XML document
# TODO: This could possibly go in parser.py, as a few defaults already do.
defaults =  {'doctype': '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">',
             'style_title':  'Xml2Rfc (sans serif)',
            }

class HtmlRfcWriter(RawTextRfcWriter):
    """ Writes to an HTML with embedded CSS """

    def __init__(self, xmlrfc, css_document='templates/rfc.css',
                 expanded_css=True, lang='en'):
        RawTextRfcWriter.__init__(self, xmlrfc)
        self.html = E.html(lang=lang)
        self.css_document = css_document
        self.expanded_css = expanded_css
        
        # Create head element, add style/metadata/etc information
        self.html.append(self.build_head())
        
        # Create body element -- everything will be added to this
        self.body = E.body()
        self.html.append(self.body)
        
    def build_stylesheet(self):
        """ Returns either a <link> or <style> element for css data.
        
            The element returned is dependent on the value of expanded_css
        """
        if self.expanded_css:
            file = open(self.css_document, 'r')
            element = E.style(file.read(), title=defaults['style_title'])
        else:
            element = E.link(rel='stylesheet', href=self.css_document)
        element.attrib['type'] = 'text/css'
        return element
    
    def build_head(self):
        """ Returns the constructed <head> element """
        head = E.head()
        head.append(self.build_stylesheet())
        return head

    # -----------------------------------------
    # Base writer interface methods to override
    # -----------------------------------------
    
    def mark_toc(self):
        raise NotImplementedError('Must override!')
    
    def write_raw(self, text, align='left'):
        raise NotImplementedError('Must override!')
        
    def write_label(self, text, align='center'):
        raise NotImplementedError('Must override!')
    
    def write_title(self, title, docName=None):
        raise NotImplementedError('Must override!')
        
    def write_heading(self, text):
        raise NotImplementedError('Must override!')

    def write_paragraph(self, text, align='left'):
        raise NotImplementedError('Must override!')

    def write_list(self, list):
        raise NotImplementedError('Must override!')

    def write_top(self, left_header, right_header):
        """ Adds the header table """
        table = E.table()
        table.attrib['class'] = 'header'
        tbody = E.tbody()
        for i in range(max(len(left_header), len(right_header))):
            if i < len(left_header):
                left_string = left_header[i]
            else:
                left_string = ''
            if i < len(right_header):
                right_string = right_header[i]
            else:
                right_string = ''
            td_left = E.td(left_string)
            td_left.attrib['class'] = 'left'
            td_right = E.td(right_string)
            td_right.attrib['class'] = 'right'
            tbody.append(E.tr(td_left, td_right))
        table.append(tbody)
        self.body.append(table)
    
    def write_address_card(self, author):
        raise NotImplementedError('Must override!')
    
    def write_reference_list(self, list):
        raise NotImplementedError('Must override!')
    
    def draw_table(self, table):
        raise NotImplementedError('Must override!')
    
    def expand_refs(self, element):
        raise NotImplementedError('Must override!')
    
    def add_to_toc(self, bullet, title, anchor=None):
        raise NotImplementedError('Must override!')
    
    def write_to_file(self, filename):
        # Write the tree to the file
        file = open(filename, 'w')
        file.write(defaults['doctype'] + '\n')
        file.write(lxml.etree.tostring(self.html, pretty_print=True))
