#converter from obj file data to simple  python dataset
source_file_name="C:/Users/antono2/Google Drive/houdiniEssentials/orient_box_line.obj"
dest_file_name="C:/Users/antono2/Google Drive/houdiniEssentials/orient_box_line.py"
source_file=open(source_file_name,"r")
dest_file=open(dest_file_name,"w")

#start class file

init_lines=r"""class lineCube:
    def __init__(self):
        self.vertices = ("""
print init_lines
dest_file.write(init_lines)
dest_file.write("\n")

vertexes_line= """"""
for line in source_file:
    if line[0]=="v":
        vertex_data_str=(line.split(" ")[1:])
        vertex_data=tuple([float(i) for i in vertex_data_str])
        vertexes_line+= "          " + str(vertex_data) + ",\n"

print vertexes_line
dest_file.write(vertexes_line)
print """        )"""
dest_file.write("        )\n")
source_file.seek(0)

#faces(lines) part
print """        self.edges = ("""
dest_file.write("        self.edges = (\n")


faces_line=""
for line in source_file:
    if line[0]=="l":
        print "line here"
        face_data_str=(line.split(" ")[1:])
        face_data=tuple([int(i) for i in face_data_str])
        faces_line+= "          " + str(face_data) + ",\n"
print faces_line
dest_file.write(faces_line)
print """        )"""
dest_file.write("""        )""")

dest_file.close()
source_file.close()


