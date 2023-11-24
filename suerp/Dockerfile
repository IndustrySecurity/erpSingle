# 使用Python官方镜像作为基础镜像
FROM python:3.9

# 设置环境变量，防止Python将文件写到容器内存中
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 设置工作目录为/app
WORKDIR /app

# 将依赖文件拷贝到容器中
COPY requirements.txt /app/

# 使用pip安装依赖
RUN apt install nc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

# 拷贝当前目录下的所有文件到容器的/app目录
COPY . /app/

# 暴露端口8000供访问
EXPOSE 8000

# 运行Django应用
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "suerp.wsgi:application"]
