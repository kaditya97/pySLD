from style.style import Style
from style.classification import Classification
import random
import numpy as np
from style.featureLabel import FeatureLabel
# from style.pointStyle import PointStyle
# from style.lineStyle import LineStyle
# from style.style import RasterStyle
# from style.polygonStyle import PolygonStyle
from style.simpleStyle import SimpleStyle
from style.classifiedStyle import ClassifiedStyle

f = FeatureLabel('jkama')

# style = Style('ear_test1', attribute_name='BU')

# values = [random.random()*5000 for _ in range(12000)]
# clf = Classification(values=values, number_of_class=5)

# c = clf.jenks_breaks()
# c = clf.geometrial_interval()
# # print(c)

# values = np.linspace(1, 66, 66)
# std = np.std(values)
# # print(c)
# x = [1, 1, 3, 4, 5, 5, 8, 9, 7]
# # y = getJenksBreaks(x, 3)
# conn = style.connect_postgres(
#     'sdssv2', password='gicait123', host='203.159.29.45')

# style.set_postgres_schema('geoinformatics_center')
# a = style.classification()
# print(a)

# style = PolygonStyle()
# s = style.classified_style(
#     'kamal', [5, 3, 43, 50, 234, 543, 821, 1114, 4542], 3)
# #

# c_ramp = {
#     'label 1 value': '#ffff55',
#     'label 2 value': '#505050',
#     'label 3 value': '#404040',
#     'label 4 value': '#333333'
# }

# color_palette = ['#333333', '#ff0000', '#ffffff', '#739747', '#342322']
attribute_name = 'kamal'
attribute_values = [5, 3, 43, 50, 234, 543, 821, 1114, 4542]
# # color_palette = ColorPalette(
# #     color_palette=c_ramp, number_of_class=7)

# rs = RasterStyle(color_palette='Spectral')
# r = rs.coverage_style()

# style = SimpleStyle()
# po_s = style.simple_point_style()
# li_s = style.simple_line_style()
# polygon_s = style.polygon_simple_style()
cs = ClassifiedStyle(attribute_name, attribute_values, feature_label=True)

print(cs.classified_style())

# print(po_s, li_s, polygon_s, style.__dict__)

# rs.color_palette_selector()
# print(rs.__dict__, r)