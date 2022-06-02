# obj file loader

from OpenGL.GL import *
class obj_loader:
    """

    OBJ models loader, supports vertices ages and polygons
    Does not support UV or curves yet
    """
    def __init__(self,obj_file_name):
        """

        :param obj_file_name: obj format model file name
        :type obj_file_name: string
        """
        import os
        if os.access(obj_file_name, os.R_OK):
            with open(obj_file_name,"r") as obj_file:
                #read components
                self.vertexes=[]
                self.lines=[]
                self.faces=[]
                for line in obj_file:
                    if line[0] == "v":
                        vertex_data_str = (line.split(" ")[1:])
                        vertex_data = tuple([float(i) for i in vertex_data_str])
                        self.vertexes.append(vertex_data)

                    if line[0] == "l":
                        line_data_str = (line.split(" ")[1:])
                        line_data = tuple([int(i) for i in line_data_str])
                        self.lines.append(line_data)

                    if line[0] == "f":
                        face_data_str = (line.split(" ")[1:])
                        face_data = tuple([int(i) for i in face_data_str])
                        self.faces.append(face_data)


    def draw(self):
        """

        GL draw commands
        """
        if len(self.vertexes)>0:
            if len(self.lines)>0:
                glBegin(GL_LINES)
                for line in self.lines:
                    #print line
                    for vertex in line:
                        #print vertex
                        glVertex3fv(self.vertexes[vertex-1])
                glEnd()

            if len(self.faces)>0:

                glBegin(GL_TRIANGLES)
                for face in self.faces:
                    #print face
                    for vertex in face:
                        glVertex3fv(self.vertexes[vertex-1])
                glEnd()



if __name__=="__main__":

    model=obj_loader("C:/Users/antono2/Google Drive/houdiniEssentials/orient_box.obj")

    print ("Vertex array:", "length:" , len(model.vertexes))
    print (model.vertexes)

    print ("Lines array:", "length:" , len(model.lines))
    print (model.lines)

    print ("Faces array:", "length:" , len(model.faces))
    print (model.faces)
