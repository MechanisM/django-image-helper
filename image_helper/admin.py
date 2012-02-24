class ImageAdminMixin(object):
    """
    Add this Mixin to your model Admin. Then in the list_display,
    declare 'listview_thumbnail' and your image will show.
    """

    def listview_thumbnail(self, obj):
        return "<img src='%s' height='100' alt=''>" % obj.thumbnail.url
    listview_thumbnail.allow_tags = True
