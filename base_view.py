"""
Created by 陈辰柄 
datetime:2019/8/31 12:23
Describe:
"""

from flask import Flask
from flask_admin import Admin, BaseView, expose


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


app = Flask(__name__)

admin = Admin(app)
admin.add_view(MyView(name='Hello'))
admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))


# class AnalyticsView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('analytics_index.html')
#
# admin.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))


if __name__ == '__main__':
    app.run()
