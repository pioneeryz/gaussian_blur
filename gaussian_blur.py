#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片高斯模糊处理工具
功能：对输入图片进行高斯模糊处理，并保存结果

使用方法：
    python gaussian_blur.py input.jpg output.jpg --radius 5
    python gaussian_blur.py input.jpg  # 默认输出到 input_blurred.jpg
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageFilter
except ImportError:
    print("❌ 错误：未找到 Pillow 库")
    print("请先安装：pip install Pillow")
    sys.exit(1)


def gaussian_blur_image(input_path: str, output_path: str, radius: float = 2.0) -> bool:
    """
    对图片进行高斯模糊处理
    
    参数:
        input_path: 输入图片路径
        output_path: 输出图片路径
        radius: 模糊半径，值越大越模糊
    
    返回:
        bool: 处理成功返回 True，失败返回 False
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_path):
            print(f"❌ 错误：输入文件不存在 - {input_path}")
            return False
        
        # 打开图片
        print(f"📷 正在打开图片：{input_path}")
        img = Image.open(input_path)
        
        # 显示原图信息
        print(f"   原图尺寸：{img.size[0]} x {img.size[1]}")
        print(f"   图片模式：{img.mode}")
        
        # 应用高斯模糊
        print(f"🔮 正在应用高斯模糊（半径：{radius}）...")
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=radius))
        
        # 保存图片
        print(f"💾 正在保存图片：{output_path}")
        
        # 确保输出目录存在
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"   创建输出目录：{output_dir}")
        
        # 根据输出格式保存
        output_ext = Path(output_path).suffix.lower()
        if output_ext in ['.jpg', '.jpeg']:
            blurred_img.save(output_path, 'JPEG', quality=95)
        elif output_ext == '.png':
            blurred_img.save(output_path, 'PNG')
        else:
            blurred_img.save(output_path)
        
        print(f"✅ 处理完成！")
        print(f"   输出文件：{output_path}")
        print(f"   文件大小：{os.path.getsize(output_path) / 1024:.2f} KB")
        
        return True
        
    except Exception as e:
        print(f"❌ 处理失败：{str(e)}")
        return False


def get_default_output_path(input_path: str) -> str:
    """生成默认输出文件路径"""
    path = Path(input_path)
    return str(path.parent / f"{path.stem}_blurred{path.suffix}")


def main():
    # 创建参数解析器
    parser = argparse.ArgumentParser(
        description='🔮 图片高斯模糊处理工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  python gaussian_blur.py photo.jpg                    # 使用默认参数
  python gaussian_blur.py photo.jpg output.jpg         # 指定输出文件
  python gaussian_blur.py photo.jpg -r 5               # 设置模糊半径为 5
  python gaussian_blur.py photo.jpg -r 10 -o out.jpg   # 完整参数示例
        '''
    )
    
    parser.add_argument('input', help='输入图片路径')
    parser.add_argument('output', nargs='?', help='输出图片路径（可选，默认在原文件名后添加_blurred）')
    parser.add_argument('-r', '--radius', type=float, default=2.0, 
                        help='模糊半径，默认 2.0（范围：0.1-50）')
    parser.add_argument('-o', '--output-path', dest='output_opt', 
                        help='输出图片路径（与 output 参数功能相同）')
    
    args = parser.parse_args()
    
    # 验证参数
    if args.radius < 0.1:
        print("⚠️  警告：半径过小，已调整为 0.1")
        args.radius = 0.1
    elif args.radius > 50:
        print("⚠️  警告：半径过大，已调整为 50")
        args.radius = 50.0
    
    # 确定输出路径
    output_path = args.output or args.output_opt or get_default_output_path(args.input)
    
    # 打印欢迎信息
    print("=" * 50)
    print("🔮 图片高斯模糊处理工具")
    print("=" * 50)
    
    # 执行处理
    success = gaussian_blur_image(args.input, output_path, args.radius)
    
    # 返回退出码
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
