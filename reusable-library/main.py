import webapp2
from library import UserInfo, RoomMeasurements, AreaController, VolumeController
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.wall_area = 0

        # Set classes for use in MainHandler
        user = UserInfo()
        room = RoomMeasurements()
        area = AreaController()
        volume = VolumeController()
        page = Page()

        if self.request.GET:
            # Gathering input data into the respective variables
            user.name = self.request.GET['name']
            room.length = self.request.GET['length']
            room.width  = self.request.GET['width']
            room.height = self.request.GET['height']
            # Find primer coverage
            self.primer_coverage = volume.primer_coverage
            # Find Finish coverage
            self.finish_coverage = volume.finish_coverage
            # Find room's wall area with given form data
            self.wall_area = area.find_wall_area(room.length, room.width, room.height)
            # Find ceiling with given form data
            self.ceiling_area = area.find_ceiling_area(room.length, room.width)
            # Find the volume of primer needed for the wall area
            self.wall_primer_volume = volume.find_paint_volume(self.wall_area, self.primer_coverage)
            # Find the volume of finish needed for the wall area
            self.wall_finish_volume = volume.find_paint_volume(self.wall_area, self.finish_coverage)
            # Find the unit of primer needed for wall area presentable for UI output
            self.wall_primer_unit = volume.determine_volume_unit(self.wall_primer_volume)
            # Find the unit of finish needed for wall area presentable for UI output
            self.wall_finish_unit = volume.determine_volume_unit(self.wall_finish_volume)
            print self.wall_finish_unit
            # Find the volume of primer needed for the ceiling area
            self.ceiling_primer_volume = volume.find_paint_volume(self.ceiling_area, self.primer_coverage)
            # Find the volume of finish needed for the ceiling area
            self.ceiling_finish_volume = volume.find_paint_volume(self.ceiling_area, self.finish_coverage)
            # Find the unit of primer needed for ceiling area presentable for UI output
            self.ceiling_primer_unit = volume.determine_volume_unit(self.ceiling_primer_volume)
            # Find the unit of finish needed for ceiling area presentable for UI output
            self.ceiling_finish_unit = volume.determine_volume_unit(self.ceiling_finish_volume)
            print self.ceiling_finish_unit
            # Get User name for use in the personalized_greeting
            self.user_name = user.name
            # Storing the print_form result into the form_page variable
            results_page = page.compile_results(self.user_name)
            # Formatting the CSS variable with the preset value
            results_page = results_page.format(**locals())
            # Printing the HTML onto the page
            print results_page
            self.response.write(results_page)
        else:
            # Storing the print_form result into the form_page variable
            form_page = page.compile_form()
            # Formatting the CSS variable with the preset value
            form_page = form_page.format(**locals())
            # Printing the HTML onto the page
            self.response.write(form_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
