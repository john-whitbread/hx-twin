import ansys.fluent.core as pf

info_file = r"C:\hx-twin-cfd\server_info.txt"
session = pf.connect_to_fluent(server_info_file_name=info_file)
print("Connected. Fluent version:", session.get_fluent_version())
