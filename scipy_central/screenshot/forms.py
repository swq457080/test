from django import forms
from django.conf import settings
import logging
logger = logging.getLogger('scipycentral')

class ScreenshotForm(forms.Form):
    """
    Upload a screenshot image for the submission
    """
    spc_image_upload = forms.ImageField()

    def clean_spc_image_upload(self):
        img_size = self.cleaned_data['spc_image_upload'].size
        logger.debug("Form img_file_raw: " + self.cleaned_data['spc_image_upload'].name)
        if img_size > settings.SPC['image_max_size']:
            raise forms.ValidationError('Image file size is too large')
        else:
            return self.cleaned_data['spc_image_upload']
