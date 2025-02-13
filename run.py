import os
import subprocess


def convert_all_music():
    # 获取当前脚本的目录
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # 获取当前脚本上一级目录
    parent_dir = os.path.dirname(current_dir)
    # print(parent_dir)

    # 遍历上一级目录中的所有文件，查找 .ncm 文件
    ncm_files = [f for f in os.listdir(parent_dir) if f.endswith('.ncm')]
    # print(ncm_files)

    # 调用 ncm.exe 执行每个 .ncm 文件
    failure_list = []
    for ncm_file in ncm_files:
        ncm_file_path = os.path.join(parent_dir, ncm_file)
        try:
            # 调用 ncmc.exe
            subprocess.run([os.path.join(current_dir, 'ncmc.exe'), ncm_file_path], check=True)
        except subprocess.CalledProcessError as e:
            failure_list.append(ncm_file)
            print(f"执行失败: {ncm_file}, 错误: {e}")

    failure_num = len(failure_list)
    if (failure_num > 0):
        for file_name in failure_list:
            print(file_name)

        print(f'共计：{len(ncm_files)} 失败：{failure_num}')
    else:
        print(f'共计：{len(ncm_files)} 全部成功')


if __name__ == '__main__':
    convert_all_music()
