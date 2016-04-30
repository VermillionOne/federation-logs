from page import Page, ContentPage
class PageFinder(object):
    def get_content_page(self, new_view):
        page = Page()
        content = ContentPage()
        if new_view == '0':
            print new_view
            # Grab sovereign page concatenation
            current_view = content.print_sovereign_page()
        #if the response yields galaxy
        elif new_view == '1':
            print new_view
            # Grab sovereign page concatenation
            current_view = content.print_galaxy_page()

        #if the response yields excelsior
        elif new_view == '2':
            print new_view
            # Grab sovereign page concatenation
            current_view = content.print_excelsior_page()

        #if the response yields constitution
        elif new_view == '3':
            print new_view
            # Grab sovereign page concatenation
            current_view = content.print_constitution_page()

        #if the response yields intrepid
        elif new_view == '4':
            print new_view
            # Grab sovereign page concatenation
            current_view = content.print_intrepid_page()

        elif new_view == 'main':
            print new_view
            # Grab main page concatenation
            current_view = page.print_main_page()
            # change data back to main page

        return current_view
