from django import forms

class ExeUploadForm(forms.Form):
    app_name = forms.CharField(max_length=50, label="Application Name")
    description = forms.CharField(widget=forms.Textarea, required=False)
    exe_file = forms.FileField(label=".exe File")
