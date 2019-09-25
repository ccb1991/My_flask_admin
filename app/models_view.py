"""
Created by 陈辰柄 
datetime:2019/9/25 23:14
Describe:
"""

from flask_admin.contrib.sqla import ModelView

# Flask and Flask-SQLAlchemy initialization here


class MicroBlogModelView(ModelView):
    can_delete = False  # disable model deletion
    page_size = 10  # the number of entries to display on the list view
    can_view_details = True  # 详细信息列设置
    column_exclude_list = ['password', ]  # 排除某一列数据
    column_editable_list = ['name', 'last_name']  # 指定可编辑的列
