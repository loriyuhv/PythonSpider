/*
 Navicat Premium Data Transfer

 Source Server         : loriyuhv
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 04/11/2021 11:06:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for data
-- ----------------------------
DROP TABLE IF EXISTS `data`;
CREATE TABLE `data`  (
  `编号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `状态` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `问政问题` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `响应时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `问政时间` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `链接` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of data
-- ----------------------------
INSERT INTO `data` VALUES ('308757', '待处理', '常平文化广场管理不作为', '等待处理：27天15小时2分', '2021-11-03 22:12:56', '/political/politics/index?id=529828');
INSERT INTO `data` VALUES ('308765', '待处理', '公司严重违反劳动法不给员工购买社保福利', '等待处理：27天15小时2分', '2021-11-03 21:32:23', '/political/politics/index?id=529824');
INSERT INTO `data` VALUES ('308756', '待处理', '麻涌东江大桥堵塞和桥抖严重', '等待处理：27天15小时2分', '2021-11-03 21:18:12', '/political/politics/index?id=529823');
INSERT INTO `data` VALUES ('308755', '待处理', '常平东元路164号GEM酒吧排气抽风设备扰民', '等待处理：27天15小时2分', '2021-11-03 21:15:10', '/political/politics/index?id=529822');
INSERT INTO `data` VALUES ('308762', '待处理', '望牛墩恒大翡翠3期，何时能正常复工？预售资金监管账户是否还有钱？', '等待处理：27天15小时2分', '2021-11-03 21:10:11', '/political/politics/index?id=529820');
INSERT INTO `data` VALUES ('308759', '待处理', '泥土车罚款', '等待处理：27天15小时2分', '2021-11-03 20:15:46', '/political/politics/index?id=529818');
INSERT INTO `data` VALUES ('308761', '待处理', '广东创新科技职业技术学院形式主义封校', '等待处理：27天15小时2分', '2021-11-03 19:43:24', '/political/politics/index?id=529816');
INSERT INTO `data` VALUES ('308763', '待处理', '东莞大道立交桥西侧荒地规划', '等待处理：27天15小时2分', '2021-11-03 19:33:34', '/political/politics/index?id=529815');
INSERT INTO `data` VALUES ('308767', '待处理', '对于《中华人民共和国土地管理法实施条例》中部分条例理解不清，请具体结实', '等待处理：27天15小时2分', '2021-11-03 18:34:27', '/political/politics/index?id=529812');
INSERT INTO `data` VALUES ('308750', '待处理', '关于莞城中英文小学旁东城路段违章停车的管控', '等待处理：26天15小时2分', '2021-11-03 17:14:26', '/political/politics/index?id=529801');
INSERT INTO `data` VALUES ('308751', '待处理', '城市管理行政执法局对寮步香居明苑违建不处理', '等待处理：26天15小时2分', '2021-11-03 17:12:43', '/political/politics/index?id=529800');
INSERT INTO `data` VALUES ('308754', '待处理', '莞番高速（广龙）大岭山镇连平连马路段高架施工无任何防护措施！', '等待处理：26天15小时2分', '2021-11-03 17:10:44', '/political/politics/index?id=529799');
INSERT INTO `data` VALUES ('308746', '已受理', '麻涌恒大滨江左岸房屋质量严重质疑', '等待回复：27天9小时10分', '2021-11-03 17:04:50', '/political/politics/index?id=529798');
INSERT INTO `data` VALUES ('308749', '待处理', '关于东莞市级光伏发电补贴', '等待处理：26天15小时2分', '2021-11-03 16:48:38', '/political/politics/index?id=529794');
INSERT INTO `data` VALUES ('308737', '待处理', '消费诈骗', '等待处理：26天15小时2分', '2021-11-03 16:30:31', '/political/politics/index?id=529792');
INSERT INTO `data` VALUES ('308686', '待处理', '东莞职业技术学院形式主义封校', '等待处理：26天13小时8分', '2021-11-03 09:13:49', '/political/politics/index?id=529724');
INSERT INTO `data` VALUES ('308689', '已受理', '常平苏坑广汇市场管理服务公司不退租房押金1380元', '等待回复：27天1小时28分', '2021-11-03 08:55:26', '/political/politics/index?id=529722');
INSERT INTO `data` VALUES ('308794', '待处理', '大朗服装厂排废气', '等待处理：27天13小时8分', '2021-11-04 10:09:49', '/political/politics/index?id=529866');
INSERT INTO `data` VALUES ('308741', '已受理', '开眼镜店（个体户）需要哪些资料和技能证书？', '等待回复：27天23小时7分', '2021-11-03 15:59:18', '/political/politics/index?id=529787');
INSERT INTO `data` VALUES ('308776', '待处理', '大朗碧桂园万象松湖22栋23栋对面的半夜商铺噪音', '等待处理：27天13小时8分', '2021-11-04 02:01:49', '/political/politics/index?id=529837');
INSERT INTO `data` VALUES ('308767', '待处理', '对于《中华人民共和国土地管理法实施条例》中部分条例理解不清，请具体结实', '等待处理：27天13小时8分', '2021-11-03 18:34:27', '/political/politics/index?id=529812');
INSERT INTO `data` VALUES ('308703', '待处理', '请问城管对那些用电动车，摩托车，三轮车霸占停车位，给自己停车的行为是否不管？？是否不在城管管理范围？', '等待处理：26天13小时8分', '2021-11-03 10:51:25', '/political/politics/index?id=529743');
INSERT INTO `data` VALUES ('308696', '待处理', '人行绿灯时间太短，老人容易急得摔跤', '等待处理：26天13小时8分', '2021-11-03 08:40:13', '/political/politics/index?id=529721');
INSERT INTO `data` VALUES ('308792', '待处理', '高雄路靠近阿里山路交叉口附近路面问题', '等待处理：27天13小时8分', '2021-11-04 09:56:04', '/political/politics/index?id=529863');
INSERT INTO `data` VALUES ('308742', '已受理', '房控管理乱价乱市', '等待回复：27天7小时4分', '2021-11-03 15:57:32', '/political/politics/index?id=529786');
INSERT INTO `data` VALUES ('308744', '已受理', '房款已付清，开发商不开发票', '等待回复：27天22小时9分', '2021-11-03 15:53:13', '/political/politics/index?id=529785');
INSERT INTO `data` VALUES ('308777', '待处理', '快递是如何定价的？', '等待处理：27天13小时8分', '2021-11-04 01:26:12', '/political/politics/index?id=529836');
INSERT INTO `data` VALUES ('308778', '待处理', '南城夜宵铺长期深夜扰民，居民无法入眠！', '等待处理：27天13小时8分', '2021-11-04 00:54:33', '/political/politics/index?id=529835');
INSERT INTO `data` VALUES ('308770', '已受理', '违规经营流失了多少国家税收', '等待回复：27天22小时10分', '2021-11-03 18:12:04', '/political/politics/index?id=529811');
INSERT INTO `data` VALUES ('308709', '待处理', '投诉浦发银行信用卡万用金分期利率', '等待处理：26天13小时8分', '2021-11-03 14:34:34', '/political/politics/index?id=529766');
INSERT INTO `data` VALUES ('308704', '待处理', '107国道改扩建施工中不能根据实际情况给居益公馆小区出口预留出口？', '等待处理：26天13小时8分', '2021-11-03 10:37:00', '/political/politics/index?id=529742');
INSERT INTO `data` VALUES ('308668', '已受理', '工作时长过多（12个小时）', '等待回复：27天5小时41分', '2021-11-03 08:25:14', '/political/politics/index?id=529717');
INSERT INTO `data` VALUES ('308636', '已受理', '谢岗镇荣兴街20号荣记美食大排档噪音扰民', '等待回复：26天22小时17分', '2021-11-03 00:24:08', '/political/politics/index?id=529703');
INSERT INTO `data` VALUES ('308790', '待处理', '戙船澳新街店铺每天霸占车位', '等待处理：27天13小时8分', '2021-11-04 09:43:50', '/political/politics/index?id=529862');
INSERT INTO `data` VALUES ('308733', '已受理', '樟木头天和百货售卖发霉食品', '等待回复：27天22小时58分', '2021-11-03 15:45:17', '/political/politics/index?id=529783');
INSERT INTO `data` VALUES ('308641', '已受理', '校运会举办安排', '等待回复：26天23小时6分', '2021-11-02 18:00:53', '/political/politics/index?id=529675');
INSERT INTO `data` VALUES ('308781', '待处理', '门口违规建筑', '等待处理：27天13小时8分', '2021-11-03 23:45:45', '/political/politics/index?id=529832');
INSERT INTO `data` VALUES ('308618', '已受理', '关于人才引进补贴', '等待回复：26天5小时19分', '2021-11-02 14:56:24', '/political/politics/index?id=529642');
INSERT INTO `data` VALUES ('308771', '待处理', '大岭山领居A区电信垄断宽带业务', '等待处理：27天13小时8分', '2021-11-03 18:11:51', '/political/politics/index?id=529810');
INSERT INTO `data` VALUES ('308710', '待处理', '韵达快递公司对消费者权益极度不负责任', '等待处理：26天13小时8分', '2021-11-03 14:34:24', '/political/politics/index?id=529765');
INSERT INTO `data` VALUES ('308690', '待处理', '厚街体育公园路口红绿灯设定时间不合理', '等待处理：26天13小时8分', '2021-11-03 10:20:55', '/political/politics/index?id=529739');
INSERT INTO `data` VALUES ('308669', '已受理', '管理不到位 懒政不作为', '等待回复：27天3小时59分', '2021-11-03 08:23:27', '/political/politics/index?id=529716');
INSERT INTO `data` VALUES ('308654', '已受理', '大岭山镇元岭村菜市场脏乱差卫生堪忧', '等待回复：26天23小时59分', '2021-11-02 23:53:47', '/political/politics/index?id=529701');
INSERT INTO `data` VALUES ('308795', '待处理', '寮步高铁站的规划咨询', '等待处理：27天13小时8分', '2021-11-04 09:43:08', '/political/politics/index?id=529861');
INSERT INTO `data` VALUES ('308725', '已受理', '防止东莞房地产大落', '等待回复：27天6小时8分', '2021-11-03 15:39:40', '/political/politics/index?id=529782');
INSERT INTO `data` VALUES ('308642', '已受理', '大朗行政服务中心与东方银座中间的天桥质量卫生问题', '等待回复：26天22小时28分', '2021-11-02 17:56:45', '/political/politics/index?id=529674');
INSERT INTO `data` VALUES ('308757', '已受理', '常平文化广场管理不作为', '等待回复：27天22小时42分', '2021-11-03 22:12:56', '/political/politics/index?id=529828');
INSERT INTO `data` VALUES ('308619', '待处理', '塘厦奥园观澜誉峰别墅区违建', '等待处理：25天13小时8分', '2021-11-02 14:52:24', '/political/politics/index?id=529641');
INSERT INTO `data` VALUES ('308773', '待处理', '企石恒大悦龙台一直不退定金', '等待处理：27天13小时8分', '2021-11-03 18:01:24', '/political/politics/index?id=529808');
INSERT INTO `data` VALUES ('308724', '已受理', '凤岗天保花园淹水需要恢复挡水坡设施', '等待回复：27天4小时57分', '2021-11-03 14:30:12', '/political/politics/index?id=529764');
INSERT INTO `data` VALUES ('308691', '待处理', '请问个人想安装光伏发电，利用楼顶空间，请问贵局有啥及格的施工企业名单？', '等待处理：26天13小时8分', '2021-11-03 10:02:21', '/political/politics/index?id=529738');
INSERT INTO `data` VALUES ('308639', '已受理', '森林湖兰溪谷14-1-1303长期投毒', '等待回复：26天22小时14分', '2021-11-03 08:15:22', '/political/politics/index?id=529715');
INSERT INTO `data` VALUES ('308656', '已受理', '危险上路', '等待回复：27天0小时57分', '2021-11-02 23:10:37', '/political/politics/index?id=529699');
INSERT INTO `data` VALUES ('308803', '待处理', '适龄儿童入读民办幼儿园补贴事宜', '等待处理：27天13小时8分', '2021-11-04 09:42:56', '/political/politics/index?id=529860');
INSERT INTO `data` VALUES ('308726', '已受理', '请东莞市交通运输局解疑', '等待回复：27天5小时34分', '2021-11-03 15:39:03', '/political/politics/index?id=529781');
INSERT INTO `data` VALUES ('308633', '待处理', '占用道路', '等待处理：25天13小时8分', '2021-11-02 17:12:39', '/political/politics/index?id=529672');
INSERT INTO `data` VALUES ('308768', '待处理', '标都没投，就敢开始施工，在法庭上还嚣张的让举报', '等待处理：27天13小时8分', '2021-11-03 21:54:10', '/political/politics/index?id=529826');
INSERT INTO `data` VALUES ('308620', '待处理', '占到经营霸占车位', '等待处理：25天13小时8分', '2021-11-02 14:31:23', '/political/politics/index?id=529639');
INSERT INTO `data` VALUES ('308774', '已受理', '请问位于松山湖光大W谷的瑞思英语培训机构的性质', '等待回复：27天22小时37分', '2021-11-03 17:58:36', '/political/politics/index?id=529806');
INSERT INTO `data` VALUES ('308727', '待处理', '长安镇OPPO新研发工地非施工时间扰民', '等待处理：26天13小时8分', '2021-11-03 14:26:58', '/political/politics/index?id=529763');
INSERT INTO `data` VALUES ('308692', '已受理', '麻涌镇麻涌大桥桥底长期不断漏水', '等待回复：27天5小时18分', '2021-11-03 09:57:46', '/political/politics/index?id=529737');
INSERT INTO `data` VALUES ('308665', '已受理', '收费就不贴标，不收费就贴标！！！', '等待回复：27天0小时53分', '2021-11-03 08:10:29', '/political/politics/index?id=529714');
INSERT INTO `data` VALUES ('308672', '已受理', '寮步镇金地领峯楼盘销售不实宣传，误导消费者！', '等待回复：27天0小时20分', '2021-11-02 22:53:45', '/political/politics/index?id=529697');
INSERT INTO `data` VALUES ('308799', '待处理', '番莞高速桥头段什么时候能开通？', '等待处理：27天13小时8分', '2021-11-04 09:28:51', '/political/politics/index?id=529856');
INSERT INTO `data` VALUES ('308719', '待处理', '汽修厂长期占用行人道，严重影响群众出行', '等待处理：26天13小时8分', '2021-11-03 15:31:22', '/political/politics/index?id=529779');
INSERT INTO `data` VALUES ('308635', '已受理', '寮步镇蟠龙路东大家具前下水道井盖安装不规范，导致噪音扰民', '等待回复：26天22小时16分', '2021-11-02 17:07:05', '/political/politics/index?id=529670');
INSERT INTO `data` VALUES ('308769', '待处理', '平衡车是否可以带上公交车？', '等待处理：27天13小时8分', '2021-11-03 21:38:54', '/political/politics/index?id=529825');
INSERT INTO `data` VALUES ('308604', '待处理', '莞番高速黄泥塘收费站', '等待处理：25天13小时8分', '2021-11-02 14:08:08', '/political/politics/index?id=529637');
INSERT INTO `data` VALUES ('308775', '待处理', '“围村收费”的最新情况', '等待处理：27天13小时8分', '2021-11-03 17:37:18', '/political/politics/index?id=529804');
INSERT INTO `data` VALUES ('308728', '待处理', '东江大道河岸卫生', '等待处理：26天13小时8分', '2021-11-03 14:13:21', '/political/politics/index?id=529762');
INSERT INTO `data` VALUES ('308694', '已受理', '横沥镇神山桥附近路段整条马路碎石粒阻挡非机动车通行，一不小心打滑就会翻车', '等待回复：27天3小时57分', '2021-11-03 09:50:57', '/political/politics/index?id=529735');
INSERT INTO `data` VALUES ('308663', '已受理', '东莞通账户冻结如何解冻？', '等待回复：27天3小时14分', '2021-11-03 08:10:06', '/political/politics/index?id=529713');
INSERT INTO `data` VALUES ('308666', '已受理', '开转诊单排三四个小时队', '等待回复：26天23小时35分', '2021-11-02 21:01:22', '/political/politics/index?id=529692');
INSERT INTO `data` VALUES ('308800', '待处理', '工地通宵施工，噪声严重扰民', '等待处理：27天13小时8分', '2021-11-04 09:22:47', '/political/politics/index?id=529855');
INSERT INTO `data` VALUES ('308718', '待处理', '长安万达广场Vclub酒吧半夜扰民', '等待处理：26天13小时8分', '2021-11-03 15:29:27', '/political/politics/index?id=529778');
INSERT INTO `data` VALUES ('308627', '待处理', '东莞市塘厦镇大坪多处违章建筑，超高超宽建筑', '等待处理：25天13小时8分', '2021-11-02 16:41:36', '/political/politics/index?id=529668');
INSERT INTO `data` VALUES ('308765', '待处理', '公司严重违反劳动法不给员工购买社保福利', '等待处理：27天13小时8分', '2021-11-03 21:32:23', '/political/politics/index?id=529824');
INSERT INTO `data` VALUES ('308605', '待处理', '校车扰民', '等待处理：25天13小时8分', '2021-11-02 14:07:36', '/political/politics/index?id=529636');
INSERT INTO `data` VALUES ('308750', '待处理', '关于莞城中英文小学旁东城路段违章停车的管控', '等待处理：26天13小时8分', '2021-11-03 17:14:26', '/political/politics/index?id=529801');
INSERT INTO `data` VALUES ('308729', '待处理', '井盖躁音扰民', '等待处理：26天13小时8分', '2021-11-03 13:47:38', '/political/politics/index?id=529761');
INSERT INTO `data` VALUES ('308695', '待处理', '犀牛陂新理想幼儿园噪音严重扰民', '等待处理：26天13小时8分', '2021-11-03 09:48:01', '/political/politics/index?id=529734');
INSERT INTO `data` VALUES ('308659', '已受理', '清溪华桂园', '等待回复：26天23小时42分', '2021-11-03 07:58:27', '/political/politics/index?id=529711');
INSERT INTO `data` VALUES ('308645', '已受理', '生活用水污浊！严重影响生活！', '等待回复：26天23小时23分', '2021-11-02 20:19:07', '/political/politics/index?id=529688');
INSERT INTO `data` VALUES ('308789', '已受理', '关于南城新基社区广东省金盾服装厂排放废气的投诉', '等待回复：27天23小时11分', '2021-11-04 09:19:37', '/political/politics/index?id=529854');
INSERT INTO `data` VALUES ('308714', '已受理', '一位难求！商铺私自霸占公共车位', '等待回复：27天22小时23分', '2021-11-03 15:24:42', '/political/politics/index?id=529777');
INSERT INTO `data` VALUES ('308630', '待处理', '投诉南城英之辅外语培训中心被要求退学费时则采取“霸王条款”、故意拖延，故意刁难，态度傲慢，敷衍了事', '等待处理：25天13小时8分', '2021-11-02 16:32:42', '/political/politics/index?id=529665');
INSERT INTO `data` VALUES ('308756', '已受理', '麻涌东江大桥堵塞和桥抖严重', '等待回复：27天23小时2分', '2021-11-03 21:18:12', '/political/politics/index?id=529823');
INSERT INTO `data` VALUES ('308607', '已受理', '蔡白湿地公园', '等待回复：26天22小时58分', '2021-11-02 13:34:12', '/political/politics/index?id=529634');
INSERT INTO `data` VALUES ('308751', '已受理', '城市管理行政执法局对寮步香居明苑违建不处理', '等待回复：27天22小时28分', '2021-11-03 17:12:43', '/political/politics/index?id=529800');
INSERT INTO `data` VALUES ('308730', '已受理', '官桥滘塘城三路施工时段不合理', '等待回复：27天22小时25分', '2021-11-03 13:40:17', '/political/politics/index?id=529760');
INSERT INTO `data` VALUES ('308688', '待处理', '波利亚外国语学校噪音扰民', '等待处理：26天13小时8分', '2021-11-03 09:47:43', '/political/politics/index?id=529733');
INSERT INTO `data` VALUES ('308660', '待处理', '寮步镇教育路碧桂园公交站台乱停车', '等待处理：26天13小时8分', '2021-11-03 07:02:50', '/political/politics/index?id=529710');
INSERT INTO `data` VALUES ('308647', '待处理', '请问东莞移动是否有计划开通eSIM业务？', '等待处理：26天13小时8分', '2021-11-02 20:11:46', '/political/politics/index?id=529686');
INSERT INTO `data` VALUES ('308788', '已受理', '常平还珠沥汇景豪园旁边沙场每天日夜施工无', '等待回复：27天23小时8分', '2021-11-04 09:18:01', '/political/politics/index?id=529853');
INSERT INTO `data` VALUES ('308715', '已受理', '农民安居房报建 4米消防通道', '等待回复：27天6小时13分', '2021-11-03 15:24:06', '/political/politics/index?id=529776');
INSERT INTO `data` VALUES ('308625', '已受理', '投诉黄江镇社区卫生服务中心', '等待回复：26天6小时55分', '2021-11-02 16:21:04', '/political/politics/index?id=529664');
INSERT INTO `data` VALUES ('308755', '已受理', '常平东元路164号GEM酒吧排气抽风设备扰民', '等待回复：27天22小时42分', '2021-11-03 21:15:10', '/political/politics/index?id=529822');
INSERT INTO `data` VALUES ('308610', '已受理', '支持高一周五放学！', '等待回复：26天23小时12分', '2021-11-02 13:06:37', '/political/politics/index?id=529629');
INSERT INTO `data` VALUES ('308754', '待处理', '莞番高速（广龙）大岭山镇连平连马路段高架施工无任何防护措施！', '等待处理：26天13小时8分', '2021-11-03 17:10:44', '/political/politics/index?id=529799');
INSERT INTO `data` VALUES ('308732', '待处理', '开医保转诊单南', '等待处理：26天13小时8分', '2021-11-03 12:37:06', '/political/politics/index?id=529758');
INSERT INTO `data` VALUES ('308684', '已受理', '红荔侨苑改动道路及绿化规划', '等待回复：27天0小时30分', '2021-11-03 09:43:10', '/political/politics/index?id=529732');
INSERT INTO `data` VALUES ('308658', '已受理', '公交站点（校车上下车点）垃圾桶乱摆放', '等待回复：27天0小时22分', '2021-11-03 06:55:06', '/political/politics/index?id=529709');
INSERT INTO `data` VALUES ('308664', '已受理', '美诺健康体检不能退费', '等待回复：27天1小时24分', '2021-11-03 01:55:15', '/political/politics/index?id=529707');
INSERT INTO `data` VALUES ('308648', '已受理', '占用森林保护区山林地，常燃放鞭炮扰民', '等待回复：27天0小时42分', '2021-11-02 20:01:32', '/political/politics/index?id=529685');
INSERT INTO `data` VALUES ('308801', '待处理', '东城街道火炼树地摊火锅店凌晨1-3点还大吵大闹', '等待处理：27天13小时8分', '2021-11-04 09:17:04', '/political/politics/index?id=529852');
INSERT INTO `data` VALUES ('308712', '待处理', '路灯', '等待处理：26天13小时8分', '2021-11-03 15:16:44', '/political/politics/index?id=529774');
INSERT INTO `data` VALUES ('308626', '已受理', '投诉黄江镇社区卫生服务中心', '等待回复：26天6小时55分', '2021-11-02 16:18:13', '/political/politics/index?id=529663');
INSERT INTO `data` VALUES ('308762', '已受理', '望牛墩恒大翡翠3期，何时能正常复工？预售资金监管账户是否还有钱？', '等待回复：27天23小时39分', '2021-11-03 21:10:11', '/political/politics/index?id=529820');
INSERT INTO `data` VALUES ('308602', '已受理', '卖房，渤海银行迟迟不放款，拿不到钱，现在连小孩奶粉都买不起', '等待回复：26天22小时48分', '2021-11-02 13:02:56', '/political/politics/index?id=529627');
INSERT INTO `data` VALUES ('308746', '已受理', '麻涌恒大滨江左岸房屋质量严重质疑', '等待回复：27天7小时16分', '2021-11-03 17:04:50', '/political/politics/index?id=529798');
INSERT INTO `data` VALUES ('308734', '待处理', '居民区大排档通宵营业严重扰民', '等待处理：26天13小时8分', '2021-11-03 12:35:08', '/political/politics/index?id=529757');
INSERT INTO `data` VALUES ('308678', '待处理', '车辆违停严重。', '等待处理：26天13小时8分', '2021-11-03 09:27:22', '/political/politics/index?id=529730');
INSERT INTO `data` VALUES ('308657', '待处理', '关于建设银行客户服务不规范，涉及诱导消费者消费以及虚假宣传', '等待处理：26天13小时8分', '2021-11-03 00:59:10', '/political/politics/index?id=529706');
INSERT INTO `data` VALUES ('308649', '待处理', '马路井盖响', '等待处理：26天13小时8分', '2021-11-02 19:49:22', '/political/politics/index?id=529684');
INSERT INTO `data` VALUES ('308650', '待处理', '南开学校附近施工噪音太大，影响学生学习。', '等待处理：26天13小时8分', '2021-11-02 19:42:23', '/political/politics/index?id=529683');
INSERT INTO `data` VALUES ('308804', '待处理', '关于南城胜和鸭仔塘变相围村收费问题', '等待处理：27天13小时8分', '2021-11-04 09:15:15', '/political/politics/index?id=529848');
INSERT INTO `data` VALUES ('308787', '待处理', '阳台养鸡导致脏乱差，老鼠爬楼！', '等待处理：27天13小时8分', '2021-11-04 08:13:38', '/political/politics/index?id=529843');
INSERT INTO `data` VALUES ('308713', '已受理', '东莞市大岭山翰华学校乱收班费购买班服资料打扫卫生用品', '等待回复：27天5小时36分', '2021-11-03 15:16:31', '/political/politics/index?id=529773');
INSERT INTO `data` VALUES ('308716', '待处理', '马路大树安全', '等待处理：26天13小时8分', '2021-11-03 15:14:54', '/political/politics/index?id=529772');
INSERT INTO `data` VALUES ('308631', '待处理', '寮步广场红绿灯经常堵车', '等待处理：25天13小时8分', '2021-11-02 16:18:03', '/political/politics/index?id=529662');
INSERT INTO `data` VALUES ('308759', '待处理', '泥土车罚款', '等待处理：27天13小时8分', '2021-11-03 20:15:46', '/political/politics/index?id=529818');
INSERT INTO `data` VALUES ('308597', '待处理', '望牛墩镇下漕管理区官派村一直都不让建房！', '等待处理：25天13小时8分', '2021-11-02 12:33:09', '/political/politics/index?id=529624');
INSERT INTO `data` VALUES ('308749', '待处理', '关于东莞市级光伏发电补贴', '等待处理：26天13小时8分', '2021-11-03 16:48:38', '/political/politics/index?id=529794');
INSERT INTO `data` VALUES ('308735', '待处理', '东莞一中南门距离不足100米万科生活噪音', '等待处理：26天13小时8分', '2021-11-03 12:22:37', '/political/politics/index?id=529756');
INSERT INTO `data` VALUES ('308679', '待处理', '稻花村物业一刀切不解决停车难问题，要求将元美东路停车改为非重点路段', '等待处理：26天13小时8分', '2021-11-03 09:25:12', '/political/politics/index?id=529729');
INSERT INTO `data` VALUES ('308670', '已受理', '东莞国药集团欺诈客户', '等待回复：27天1小时28分', '2021-11-03 00:32:27', '/political/politics/index?id=529704');
INSERT INTO `data` VALUES ('308651', '待处理', '泥头车罚款扣分', '等待处理：26天13小时8分', '2021-11-02 19:35:48', '/political/politics/index?id=529682');
INSERT INTO `data` VALUES ('308785', '待处理', '失业补助金申请之后什么时候发放', '等待处理：27天13小时8分', '2021-11-04 07:04:44', '/political/politics/index?id=529842');
INSERT INTO `data` VALUES ('308717', '已受理', '塘厦镇关于强制要求家长到校门口执勤', '等待回复：27天4小时52分', '2021-11-03 15:10:13', '/political/politics/index?id=529771');
INSERT INTO `data` VALUES ('308622', '已受理', '要求家长购买教科书', '等待回复：26天6小时9分', '2021-11-02 16:01:01', '/political/politics/index?id=529658');
INSERT INTO `data` VALUES ('308761', '待处理', '广东创新科技职业技术学院形式主义封校', '等待处理：27天13小时8分', '2021-11-03 19:43:24', '/political/politics/index?id=529816');
INSERT INTO `data` VALUES ('308599', '已受理', '常平桔园街路面下陷', '等待回复：26天5小时32分', '2021-11-02 12:25:39', '/political/politics/index?id=529622');
INSERT INTO `data` VALUES ('308737', '待处理', '消费诈骗', '等待处理：26天13小时8分', '2021-11-03 16:30:31', '/political/politics/index?id=529792');
INSERT INTO `data` VALUES ('308706', '待处理', '地址门牌上没有二维码如何申请？', '等待处理：26天13小时8分', '2021-11-03 11:50:02', '/political/politics/index?id=529752');
INSERT INTO `data` VALUES ('308681', '待处理', '东城新世界花园政府推导垃圾分类半途而废', '等待处理：26天13小时8分', '2021-11-03 09:21:53', '/political/politics/index?id=529728');
INSERT INTO `data` VALUES ('308636', '已受理', '谢岗镇荣兴街20号荣记美食大排档噪音扰民', '等待回复：26天22小时17分', '2021-11-03 00:24:08', '/political/politics/index?id=529703');
INSERT INTO `data` VALUES ('308652', '已受理', '办理的银行pos机无法退回', '等待回复：26天22小时48分', '2021-11-02 19:19:05', '/political/politics/index?id=529681');
INSERT INTO `data` VALUES ('308784', '待处理', '金地前海山地下车库增加出入口问题', '等待处理：27天13小时8分', '2021-11-04 06:19:55', '/political/politics/index?id=529841');
INSERT INTO `data` VALUES ('308722', '已受理', '电脑毛织机为何这么嘈', '等待回复：27天4小时59分', '2021-11-03 14:51:03', '/political/politics/index?id=529768');
INSERT INTO `data` VALUES ('308623', '待处理', '东莞转诊制度真的方便吗', '等待处理：25天13小时8分', '2021-11-02 15:59:22', '/political/politics/index?id=529657');
INSERT INTO `data` VALUES ('308763', '待处理', '东莞大道立交桥西侧荒地规划', '等待处理：27天13小时8分', '2021-11-03 19:33:34', '/political/politics/index?id=529815');
INSERT INTO `data` VALUES ('308595', '已受理', '洪梅镇政府不顾村民建房成本高，要求效果图', '等待回复：26天5小时45分', '2021-11-02 11:47:42', '/political/politics/index?id=529618');
INSERT INTO `data` VALUES ('308736', '已受理', '万江加州花园 水管严重腐蚀 居民饮水担忧', '等待回复：27天5小时42分', '2021-11-03 16:23:26', '/political/politics/index?id=529791');
INSERT INTO `data` VALUES ('308707', '待处理', '补缴社保和公积金', '等待处理：26天13小时8分', '2021-11-03 11:48:12', '/political/politics/index?id=529751');
INSERT INTO `data` VALUES ('308682', '已受理', '寮步汽车城没有路灯', '等待回复：27天0小时33分', '2021-11-03 09:18:26', '/political/politics/index?id=529727');
INSERT INTO `data` VALUES ('308638', '待处理', '众盛物业撤出不交接，财务不公示，侵占业主利益', '等待处理：26天13小时8分', '2021-11-02 18:33:37', '/political/politics/index?id=529678');
INSERT INTO `data` VALUES ('308783', '待处理', '大岭山金地林森艺境', '等待处理：27天13小时8分', '2021-11-04 03:27:41', '/political/politics/index?id=529840');
INSERT INTO `data` VALUES ('308624', '待处理', '海逸豪庭大肆违建为何不处置、不拆除', '等待处理：25天13小时8分', '2021-11-02 15:53:36', '/political/politics/index?id=529655');
INSERT INTO `data` VALUES ('308767', '待处理', '对于《中华人民共和国土地管理法实施条例》中部分条例理解不清，请具体结实', '等待处理：27天13小时8分', '2021-11-03 18:34:27', '/political/politics/index?id=529812');
INSERT INTO `data` VALUES ('308586', '待处理', '噪音扰民', '等待处理：25天13小时8分', '2021-11-02 11:44:19', '/political/politics/index?id=529616');
INSERT INTO `data` VALUES ('308738', '已受理', '请住建局公布厚街万科臻山悦花园楼盘预售备案价过程资料，以供广大市民群众监督。', '等待回复：27天7小时7分', '2021-11-03 16:09:53', '/political/politics/index?id=529790');
INSERT INTO `data` VALUES ('308700', '已受理', '石龙中山路车位被商铺占用', '等待回复：27天6小时9分', '2021-11-03 11:34:31', '/political/politics/index?id=529750');
INSERT INTO `data` VALUES ('308683', '待处理', '私人长期霸占村内公共停车位', '等待处理：26天13小时8分', '2021-11-03 09:16:16', '/political/politics/index?id=529726');
INSERT INTO `data` VALUES ('308640', '已受理', '东莞华侨城纯水岸小区花园差', '等待回复：26天22小时25分', '2021-11-02 18:23:41', '/political/politics/index?id=529677');
INSERT INTO `data` VALUES ('308613', '待处理', '南城车站路片区城市更新', '等待处理：25天13小时8分', '2021-11-02 15:25:00', '/political/politics/index?id=529649');
INSERT INTO `data` VALUES ('308584', '待处理', '房屋外的水管阀门坏了，是水表前的阀门，由谁来负责', '等待处理：25天13小时8分', '2021-11-02 11:37:14', '/political/politics/index?id=529615');
INSERT INTO `data` VALUES ('308739', '待处理', '关于一孩生育问题咨询电话没人接听的投诉', '等待处理：26天13小时8分', '2021-11-03 16:04:21', '/political/politics/index?id=529789');
INSERT INTO `data` VALUES ('308698', '待处理', '异地门诊转诊', '等待处理：26天13小时8分', '2021-11-03 11:18:06', '/political/politics/index?id=529748');
INSERT INTO `data` VALUES ('308685', '待处理', '沙田公交213，221线路问题', '等待处理：26天13小时8分', '2021-11-03 09:15:23', '/political/politics/index?id=529725');
INSERT INTO `data` VALUES ('308653', '待处理', '关于公常公路X232与莞深高速交汇节点改造工程进展问题', '等待处理：26天13小时8分', '2021-11-02 18:14:55', '/political/politics/index?id=529676');
INSERT INTO `data` VALUES ('308600', '已受理', '茶山纳帕溪谷湘阁里辣烟雾恶臭严重影响生活', '等待回复：26天4小时47分', '2021-11-02 15:07:35', '/political/politics/index?id=529645');
INSERT INTO `data` VALUES ('308585', '待处理', '东莞理工学校  食堂定价不合理！', '等待处理：25天13小时8分', '2021-11-02 11:21:22', '/political/politics/index?id=529614');
INSERT INTO `data` VALUES ('308588', '已受理', '工作效率极低', '等待回复：26天5小时17分', '2021-11-02 11:15:09', '/political/politics/index?id=529612');
INSERT INTO `data` VALUES ('308699', '已受理', '万江胜利社区围村停车收费不合理', '等待回复：27天0小时59分', '2021-11-03 11:08:19', '/political/politics/index?id=529747');
INSERT INTO `data` VALUES ('308617', '已受理', '桥头镇桥龙路温馨家园鸿华尚城4栋.5栋管理处滥收居民电费', '等待回复：26天5小时33分', '2021-11-02 15:02:05', '/political/politics/index?id=529643');

SET FOREIGN_KEY_CHECKS = 1;
