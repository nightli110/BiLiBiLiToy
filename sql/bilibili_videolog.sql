/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.1.49
 Source Server Type    : MySQL
 Source Server Version : 50730
 Source Host           : 192.168.1.49:3306
 Source Schema         : bilibilidata

 Target Server Type    : MySQL
 Target Server Version : 50730
 File Encoding         : 65001

 Date: 24/05/2022 22:43:52
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bilibili_videolog
-- ----------------------------
DROP TABLE IF EXISTS `bilibili_videolog`;
CREATE TABLE `bilibili_videolog`  (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '标题',
  `date` datetime NULL DEFAULT NULL COMMENT '时间',
  `videoid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '视频id',
  `visit` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '播放量',
  `barrage` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '播放量',
  `rank` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '排名',
  `daydate` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '天日期',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `uk_title`(`title`) USING BTREE,
  INDEX `uk_daydate`(`daydate`) USING BTREE,
  INDEX `uk_daydate_rank`(`rank`, `daydate`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
