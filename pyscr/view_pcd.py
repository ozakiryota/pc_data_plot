import argparse
import glob
import open3d

class ViewPcd:
    def __init__(self):
        self.arg_parser = argparse.ArgumentParser()
        self.args = self.setArgument()
        self.target_extension = ['pcd']

    def setArgument(self):
        self.arg_parser.add_argument('--pcd_path', required=True)
        return self.arg_parser.parse_args()

    def view(self):
        pcd_path_list = self.getPcdPathList()
        pcd_list = []
        for pcd_path in pcd_path_list:
            pcd = open3d.io.read_point_cloud(pcd_path)
            pcd_list.append(pcd)
        open3d.visualization.draw_geometries(pcd_list)

    def getPcdPathList(self):
        pcd_path_list = []
        file_list = glob.glob(self.args.pcd_path)
        for file_path in file_list:
            extension = file_path.split('.')[-1]
            if extension in self.target_extension:
                pcd_path_list.append(file_path)
        return pcd_path_list

if __name__ == '__main__':
    view_pcd = ViewPcd()
    view_pcd.view()