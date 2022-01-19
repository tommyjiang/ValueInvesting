# 股价数据
yanghe_now = 155.00
yanghe_max = 500

# 洋河股份
yanghe_guben = 15.06988

yanghe_shizhi = [(2100, '理想买点'),
                 (2500, '合理估值下限'),
                 (2750, '合理估值中值'),
                 (3000, '合理估值上限'),
                 (4200, '三年后合理估值'),
                 (5000, '一年内第一卖点'),
                 (5500, '一年内第二卖点'),
                 (6000, '一年内第三卖点'),]

yanghe_shizhi.append((yanghe_now * yanghe_guben, '当前市值'))

yanghe_gujia = [(round(x[0] / yanghe_guben, 2), x[1]) for x in yanghe_shizhi]
yanghe_gujia.sort()

yanghe_zuobiao = [(round(x[0] * 18 / yanghe_max, 2), x[1]) for x in yanghe_gujia]

print("洋河股价", yanghe_gujia)
print("tikz 坐标", yanghe_zuobiao)

