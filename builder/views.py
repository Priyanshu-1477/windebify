from django.shortcuts import render
from .forms import ExeUploadForm
from django.conf import settings
import os
from .utils import build_deb_package
from django.contrib.auth.decorators import login_required

  # if you put it in builder.py
@login_required(login_url='login')
def upload_exe(request):
    if request.method == 'POST':
        form = ExeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            app_name = form.cleaned_data['app_name']
            description = form.cleaned_data['description']
            exe_file = request.FILES['exe_file']

            # Save the uploaded file to media/ directory
            exe_path = os.path.join(settings.MEDIA_ROOT, exe_file.name)
            with open(exe_path, 'wb+') as dest:
                for chunk in exe_file.chunks():
                    dest.write(chunk)

            # Call function to build the .deb package
            deb_file = build_deb_package(app_name, exe_file.name, description)

            # Return success page with download link
            return render(request, 'builder/success.html', {
                'app_name': app_name,
                'exe_path': exe_path,
                'deb_file': deb_file
            })

    else:
        form = ExeUploadForm()

    return render(request, 'builder/upload.html', {"form": form})
import subprocess
import shutil
from pathlib import Path
@login_required(login_url='login')

def build_deb_package(app_name, exe_filename, description):
    base_path = Path("debuild") / app_name
    debian_path = base_path / "DEBIAN"
    opt_path = base_path / "opt" / app_name
    bin_path = base_path / "usr" / "bin"
    desktop_path = base_path / "usr" / "share" / "applications"

    # Clear any existing package with the same name
    if base_path.exists():
        shutil.rmtree(base_path)

    # Create required directories
    debian_path.mkdir(parents=True)
    opt_path.mkdir(parents=True)
    bin_path.mkdir(parents=True)
    desktop_path.mkdir(parents=True)

    # Move uploaded exe into /opt/<app_name>/
    source_exe = Path("media") / exe_filename
    dest_exe = opt_path / exe_filename
    shutil.copy(source_exe, dest_exe)

    # Write control file
    control_content = (
        f"Package: {app_name.lower()}\n"
        f"Version: 1.0\n"
        f"Section: base\n"
        f"Priority: optional\n"
        f"Architecture: all\n"
        f"Depends: wine\n"
        f"Maintainer: You <you@example.com>\n"
        f"Description: {description or 'A Windows app packed into .deb'}\n"
    )

    with open(debian_path / "control", "w") as f:
        f.write(control_content)

    # Write Wine launcher script
    launcher_script = f"""#!/bin/bash
wine /opt/{app_name}/{exe_filename}
"""
    launcher_file = bin_path / app_name
    with open(launcher_file, "w") as f:
        f.write(launcher_script)
    launcher_file.chmod(0o755)

    # Write desktop shortcut
    desktop_entry = f"""
[Desktop Entry]
Name={app_name}
Exec={app_name}
Type=Application
Icon=application-x-executable
Categories=Utility;
"""
    with open(desktop_path / f"{app_name}.desktop", "w") as f:
        f.write(desktop_entry.strip())

    # Build .deb
    deb_file = f"{app_name}.deb"
    subprocess.run(["dpkg-deb", "--build", str(base_path), deb_file], check=True)

    # Move .deb file to media folder so Django can serve it
    deb_file_path = os.path.join(settings.MEDIA_ROOT, deb_file)
    shutil.move(deb_file, deb_file_path)

    # Build URL for the frontend
    deb_file_url = os.path.join(settings.MEDIA_URL, deb_file)

    return deb_file_url  # <- now you return the full URL instead of just filename

    deb_file_url = build_deb_package(app_name, exe_file.name, description)

    return render(request, 'builder/success.html', context)
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'builder/dashboard.html')
@login_required(login_url='login')

def my_builds(request):
    return render(request, 'builder/my_builds.html')

# Create your views here.
