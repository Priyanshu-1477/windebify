import os

def build_deb_package(app_name, exe_filename, description):
    # dummy .deb creation
    deb_filename = f"{app_name}.deb"
    deb_path = os.path.join("media", deb_filename)

    with open(deb_path, "w") as f:
        f.write(f"This is a fake .deb file for {app_name}\n")
        f.write(f"Original .exe: {exe_filename}\n")
        f.write(f"Description: {description}\n")

    return deb_path
