import argparse
import shutil
import glob
import open3d
import numpy as np
import os
import matplotlib.pyplot as plt

class PlotPcd:
    def __init__(self):
        self.arg_parser = argparse.ArgumentParser()
        self.args = self.setArgument()
        self.target_extension = ['pcd']

    def setArgument(self):
        self.arg_parser.add_argument('--pcd_path', required=True)
        self.arg_parser.add_argument('--save_dir', default='../save')
        self.arg_parser.add_argument('--flag_merge', action='store_true')
        self.arg_parser.add_argument('--x_min', type=float)
        self.arg_parser.add_argument('--x_max', type=float)
        self.arg_parser.add_argument('--y_min', type=float)
        self.arg_parser.add_argument('--y_max', type=float)
        self.arg_parser.add_argument('--z_min', type=float)
        self.arg_parser.add_argument('--z_max', type=float)
        return self.arg_parser.parse_args()

    def main(self):
        shutil.rmtree(self.args.save_dir, ignore_errors=True)

        pcd_path_list = self.getPcdList()
        points_x_list = []
        points_y_list = []
        points_z_list = []
        # print('pcd_path_list =', pcd_path_list)

        for pcd_path in pcd_path_list:
            pcd = open3d.io.read_point_cloud(pcd_path)
            points = np.asarray(pcd.points)
            if self.args.flag_merge:
                points_x_list.append(points[:, 0])
                points_y_list.append(points[:, 1])
                points_z_list.append(points[:, 2])
            else:
                pcd_name = os.path.splitext(os.path.basename(pcd_path))[0]
                self.plotAndSave(
                    os.path.join(pcd_name, 'yx.png'),
                    'y [m]', 'x [m]',
                    [points[:, 1]], [points[:, 0]],
                    invert_x_axis=True,
                    xlim=[self.args.y_min, self.args.y_max], ylim=[self.args.x_min, self.args.x_max]
                )
                self.plotAndSave(
                    os.path.join(pcd_name, 'yz.png'),
                    'y [m]', 'z [m]',
                    [points[:, 1]], [points[:, 2]],
                    invert_x_axis=True,
                    xlim=[self.args.y_min, self.args.y_max], ylim=[self.args.z_min, self.args.z_max]
                )
                self.plotAndSave(
                    os.path.join(pcd_name, 'xz.png'),
                    'x [m]', 'z [m]',
                    [points[:, 0]], [points[:, 2]],
                    invert_x_axis=False,
                    xlim=[self.args.x_min, self.args.x_max], ylim=[self.args.z_min, self.args.z_max]
                )
        if self.args.flag_merge:
            self.plotAndSave(
                'yx.png',
                'y [m]', 'x [m]',
                points_y_list, points_x_list,
                invert_x_axis=True,
                xlim=[self.args.y_min, self.args.y_max], ylim=[self.args.x_min, self.args.x_max]
            )
            self.plotAndSave(
                'yz.png',
                'y [m]', 'z [m]',
                points_y_list, points_z_list,
                invert_x_axis=True,
                xlim=[self.args.y_min, self.args.y_max], ylim=[self.args.z_min, self.args.z_max]
            )
            self.plotAndSave(
                'xz.png',
                'x [m]', 'z [m]',
                points_x_list, points_z_list,
                invert_x_axis=False,
                xlim=[self.args.x_min, self.args.x_max], ylim=[self.args.z_min, self.args.z_max]
            )
        # plt.show()

    def getPcdList(self):
        pcd_path_list = []
        file_list = glob.glob(self.args.pcd_path)
        for file_path in file_list:
            extension = file_path.split('.')[-1]
            if extension in self.target_extension:
                pcd_path_list.append(file_path)
        return pcd_path_list

    def plotAndSave(self, save_name, x_label, y_label, x_data_list, y_data_list, invert_x_axis=False, invert_y_axis=False, xlim=[None, None], ylim=[None, None]):
        ## path
        save_path = os.path.join(self.args.save_dir, save_name)
        save_dir = os.path.dirname(save_path)
        ## figure
        plt.figure()
        sub = plt.subplot()
        ## label
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        ## data
        for x_data, y_data in zip(x_data_list, y_data_list):
            plt.scatter(x_data, y_data, s=1)
        ## axis
        if (xlim[0] is not None) and (xlim[1] is not None):
            sub.set_xlim(xlim)
        if (ylim[0] is not None) and (ylim[1] is not None):
            sub.set_ylim(ylim)
        if invert_x_axis:
            sub.invert_xaxis()
        if invert_y_axis:
            sub.invert_yaxis()
        sub.set_aspect('equal')
        ## save
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(save_path)
        print('Save:', save_path)

if __name__ == '__main__':
    plot_pcd = PlotPcd()
    plot_pcd.main()