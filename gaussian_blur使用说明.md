# Gaussian Blur 图片模糊处理工具

> 🔮 一个简单易用的图片高斯模糊处理脚本

---

## 简介

`gaussian_blur.py` 是一个基于 Python 的图片处理脚本，使用 Pillow 库对图片应用高斯模糊效果。支持自定义模糊强度，自动生成输出文件名，适用于批量处理或快速模糊图片。

---

## 功能特点

- ✅ 支持 JPG/JPEG/PNG 等常见图片格式
- ✅ 可自定义模糊半径（强度）
- ✅ 自动生成输出文件名
- ✅ 自动创建输出目录
- ✅ 显示处理进度和文件信息
- ✅ 完善的错误处理和参数验证

---

## 安装依赖

### 环境要求

- Python 3.6+
- Pillow 库

### 安装 Pillow

```bash
pip install Pillow
```

或使用国内镜像加速：

```bash
pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

## 使用方法

### 基本语法

```bash
python gaussian_blur.py <输入图片> [输出图片] [选项]
```

### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `input` | 输入图片路径（必需） | - |
| `output` | 输出图片路径（可选） | `<原文件名>_blurred.<原扩展名>` |
| `-r, --radius` | 模糊半径，值越大越模糊 | `2.0` |
| `-o, --output-path` | 输出路径（与 output 功能相同） | - |

### 模糊半径说明

- 范围：**0.1 ~ 50**
- 值越大，模糊效果越强
- 推荐范围：
  - `1-3`：轻微模糊，保留轮廓
  - `5-10`：中等模糊，适合隐私遮挡
  - `15-30`：强模糊，面部识别困难
  - `>30`：极强模糊，几乎无法辨认

---

## 使用示例

### 1. 基本使用（默认参数）

```bash
python gaussian_blur.py photo.jpg
```

输出：`photo_blurred.jpg`（模糊半径 2.0）

---

### 2. 指定输出文件名

```bash
python gaussian_blur.py photo.jpg output.jpg
```

或使用 `-o` 参数：

```bash
python gaussian_blur.py photo.jpg -o output.jpg
```

---

### 3. 自定义模糊强度

```bash
# 轻微模糊
python gaussian_blur.py photo.jpg -r 3

# 中等模糊（适合隐私遮挡）
python gaussian_blur.py photo.jpg -r 10

# 强模糊
python gaussian_blur.py photo.jpg -r 25

# 极强模糊
python gaussian_blur.py photo.jpg -r 50
```

---

### 4. 完整参数示例

```bash
python gaussian_blur.py /path/to/input.png -r 15 -o /path/to/output.png
```

---

### 5. 处理不同格式

```bash
# JPG 格式
python gaussian_blur.py image.jpg -r 5

# PNG 格式（保留透明度）
python gaussian_blur.py image.png -r 5

# 其他格式
python gaussian_blur.py image.bmp -r 5
```

---

## 输出示例

```
==================================================
🔮 图片高斯模糊处理工具
==================================================
📷 正在打开图片：photo.jpg
   原图尺寸：1920 x 1080
   图片模式：RGB
🔮 正在应用高斯模糊（半径：5.0）...
💾 正在保存图片：photo_blurred.jpg
✅ 处理完成！
   输出文件：photo_blurred.jpg
   文件大小：245.67 KB
```

---

## 批量处理

### Shell 脚本批量处理

```bash
#!/bin/bash
# 批量模糊当前目录下所有 JPG 图片

for file in *.jpg; do
    python gaussian_blur.py "$file" -r 10
done
```

### PowerShell 批量处理

```powershell
# 批量模糊当前目录下所有 JPG 图片
Get-ChildItem *.jpg | ForEach-Object {
    python gaussian_blur.py $_.Name -r 10
}
```

### Python 批量处理脚本

```python
import os
import subprocess

# 批量处理文件夹中的图片
input_dir = "./images"
output_dir = "./blurred"
radius = 10

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        cmd = [
            'python', 'gaussian_blur.py',
            input_path, '-r', str(radius), '-o', output_path
        ]
        subprocess.run(cmd)
```

---

## 常见问题

### Q1: 提示 "未找到 Pillow 库"

**错误信息：**
```
❌ 错误：未找到 Pillow 库
请先安装：pip install Pillow
```

**解决方法：**
```bash
pip install Pillow
```

---

### Q2: 输入文件不存在

**错误信息：**
```
❌ 错误：输入文件不存在 - photo.jpg
```

**解决方法：**
- 检查文件路径是否正确
- 确保文件存在
- 使用绝对路径：`python gaussian_blur.py /full/path/to/photo.jpg`

---

### Q3: 模糊半径警告

**警告信息：**
```
⚠️  警告：半径过小，已调整为 0.1
⚠️  警告：半径过大，已调整为 50
```

**说明：**
- 脚本会自动修正超出范围的值
- 模糊半径范围：0.1 ~ 50

---

### Q4: 输出目录自动创建

如果指定的输出目录不存在，脚本会自动创建：

```
💾 正在保存图片：./output/blurred/photo.jpg
   创建输出目录：./output/blurred
```

---

## 技术细节

### 支持的图片格式

| 格式 | 扩展名 | 保存质量 |
|------|--------|----------|
| JPEG | .jpg, .jpeg | quality=95 |
| PNG | .png | 无损压缩 |
| BMP | .bmp | 默认设置 |
| 其他 | - | 默认设置 |

### 处理流程

1. 检查输入文件是否存在
2. 打开图片并获取信息
3. 应用高斯模糊滤镜
4. 创建输出目录（如需要）
5. 根据格式保存图片
6. 显示处理结果

---

## 退出码

| 退出码 | 说明 |
|--------|------|
| 0 | 处理成功 |
| 1 | 处理失败 |

可用于脚本中判断处理结果：

```bash
python gaussian_blur.py photo.jpg -r 5
if [ $? -eq 0 ]; then
    echo "处理成功"
else
    echo "处理失败"
fi
```

---

## 隐私保护建议

高斯模糊常用于保护隐私（如遮挡人脸、车牌、敏感信息）：

### 遮挡人脸

```bash
python gaussian_blur.py face.jpg -r 15
```

### 遮挡车牌

```bash
python gaussian_blur.py car.jpg -r 20
```

### 遮挡敏感文字

```bash
python gaussian_blur.py document.jpg -r 10
```

> ⚠️ **注意**：对于局部遮挡，建议使用图像编辑软件（如 Photoshop、GIMP）或专门的隐私保护工具。

---

## 相关资源

- [Pillow 官方文档](https://pillow.readthedocs.io/)
- [高斯模糊算法原理](https://zh.wikipedia.org/wiki/%E9%AB%98%E6%96%AF%E6%A8%A1%E7%B3%8A)

---

## 更新日志

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | - | 初始版本 |

---

## 许可证

本脚本仅供学习和个人使用。

---

*创建日期：2024-01-15*