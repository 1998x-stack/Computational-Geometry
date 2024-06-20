import os
lectures = {
  "1_计算几何_导言": [
    "1.1_凸包的例子",
    "1.2_退化及鲁棒性",
    "1.3_应用领域",
    "1.4_注释及评论",
  ],
  "2_线段求交_专题图叠合": [
    "2.1_线段求交",
    "2.2_双向链接边表",
    "2.3_计算子区域划分的叠合",
    "2.4_布尔运算",
    "2.5_注释及评论",
  ],
  "3_多边形三角剖分_画廊看守": [
    "3.1_看守与三角剖分",
    "3.2_多边形的单调块划分",
    "3.3_单调多边形的三角剖分",
    "3.4_注释及评论",
  ],
  "4_线性规划_铸模制造": [
    "4.1_铸造中的几何",
    "4.2_半平面求交",
    "4.3_递增式线性规划",
    "4.4_随机线性规划",
    "4.5_无界线性规划问题",
    "4.6_高维空间中的线性规划",
    "4.7_最小包围圆",
    "4.8_注释及评论",
  ],
  "5_正交区域查找_数据库查询": [
    "5.1_一维区域查找",
    "5.2_kd_树",
    "5.3_区域树",
    "5.4_高维区域树",
    "5.5_一般性点集",
    "5.6_分散层叠",
    "5.7_注释及评论",
  ],
  "6_点定位_找到自己的位置": [
    "6.1_点定位及梯形图",
    "6.2_随机增量式算法",
    "6.3_退化情况的处理",
    "6.4_尾分析",
    "6.5_注释及评论",
  ],
  "7_Voronoi图_邮局问题": [
    "7.1_定义及基本性质",
    "7.2_构造Voronoi图",
    "7.3_线段集Voronoi图",
    "7.4_最远点Voronoi图",
    "7.5_注释及评论",
  ],
  "8_排列与对偶_光线跟踪超采样": [
    "8.1_差异值的计算",
    "8.2_对偶变换",
    "8.3_直线的排列",
    "8.4_层阶与偏差",
    "8.5_注释及评论",
  ],
  "9_Delaunay三角剖分_高度插值": [
    "9.1_平面点集的三角剖分",
    "9.2_Delaunay三角剖分",
    "9.3_构造Delaunay三角剖分",
    "9.4_分析",
    "9.5_随机算法框架",
    "9.6_注释及评论",
  ],
  "10_更多几何数据结构_截窗": [
    "10.1_区间树",
    "10.2_优先查找树",
    "10.3_线段树",
    "10.4_注释及评论",
  ],
  "11_凸包_混合物": [
    "11.1_三维凸包的复杂度",
    "11.2_构造三维凸包",
    "11.3_分析",
    "11.4_凸包与半空间求交",
    "11.5_再论Voronoi图",
    "11.6_注释及评论",
  ],
  "12_空间二分_画家算法": [
    "12.1_BSP树的定义",
    "12.2_BSP树及画家算法",
    "12.3_构造BSP树",
    "12.4_三维BSP树的规模",
    "12.5_低密度场景的BSP树",
    "12.6_注释及评论",
  ],
  "13_机器人运动规划_随意所之": [
    "13.1_工作空间与C_空间",
    "13.2_点机器人",
    "13.3_Minkowski和",
    "13.4_平移式运动规划",
    "13.5_允许旋转的运动规划",
    "13.6_注释及评论",
  ],
  "14_四叉树_非均匀网格生成": [
    "14.1_均匀及非均匀网格",
    "14.2_点集的四叉树",
    "14.3_从四叉树到网格",
    "14.4_注释及评论",
  ],
  "15_可见性图_求最短路径": [
    "15.1_点机器人的最短路径",
    "15.2_构造可见性图",
    "15.3_平移运动多边形机器人的最短路径",
    "15.4_注释及评论",
  ],
  "16_单纯形区域查找_再论截窗": [
    "16.1_划分树",
    "16.2_多层划分树",
    "16.3_切分树",
    "16.4_注释及评论",
  ]
}
# 创建目录和文件
for lecture_id_name, contents in lectures.items():
    lecture_id_name = lecture_id_name.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "")
    # 创建目录
    os.makedirs(lecture_id_name, exist_ok=True)
    for content in contents:
        # 文件名不能有空格和特殊字符，替换为下划线
        file_name = content.replace(" ", "_").replace("-", "_").replace(",", "") + ".py"
        file_path = os.path.join(lecture_id_name, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {content}\n\n")
            file.write(f'"""\n\nLecture: {lecture_id_name}\nContent: {content}\n\n"""\n\n')
            
        file_name = content.replace(" ", "_").replace("-", "_").replace(",", "") + ".md"
        file_path = os.path.join(lecture_id_name, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {content}\n\n")
            file.write(f'"""\n\nLecture: {lecture_id_name}\nContent: {content}\n\n"""\n\n')
        
    readme_file_path = os.path.join(lecture_id_name, "README.md")
    with open(readme_file_path, 'w', encoding='utf-8') as file:
        file.write(f"# {lecture_id_name}\n\n")
        file.write(f'"""\nLecture: {lecture_id_name}\n"""\n\n')
        for content in contents:
            file.write(f"## {content}\n\n")
# 创建目录和文件并生成README.md
with open("README.md", 'w', encoding='utf-8') as readme_file:
    readme_file.write("# Computer Vision\n\n")
    readme_file.write("This is a repository for computer vision learning.\n\n")
    
    for lecture_id_name, contents in lectures.items():
        lecture_id_name = lecture_id_name.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "")
        # 创建目录
        os.makedirs(lecture_id_name, exist_ok=True)
        
        # 在README中添加章节标题
        readme_file.write(f"## {lecture_id_name}\n\n")
        
        for content in contents:
            # 文件名不能有空格和特殊字符，替换为下划线
            file_name = content.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "") + ".py"
            file_path = os.path.join(lecture_id_name, file_name)
            
            # 创建文件并写入初始内容
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {content}\n\n")
                file.write(f'"""\nLecture: {lecture_id_name}\nContent: {content}\n"""\n\n')
            
            # 在README中添加文件链接
            readme_file.write(f"- [{content}](./{lecture_id_name}/{file_name})\n")
            
            readme_file.write("\n")
            
            
            # 文件名不能有空格和特殊字符，替换为下划线
            file_name = content.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "") + ".md"
            file_path = os.path.join(lecture_id_name, file_name)
            
            # 创建文件并写入初始内容
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {content}\n\n")
                file.write(f'"""\nLecture: {lecture_id_name}\nContent: {content}\n"""\n\n')
            
            # 在README中添加文件链接
            readme_file.write(f"- [{content}](./{lecture_id_name}/{file_name})\n")
        
        # 添加空行以分隔不同的lecture
        readme_file.write("\n")
print("目录和文件创建完成。")