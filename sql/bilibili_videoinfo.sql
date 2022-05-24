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

 Date: 24/05/2022 22:43:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bilibili_videoinfo
-- ----------------------------
DROP TABLE IF EXISTS `bilibili_videoinfo`;
CREATE TABLE `bilibili_videoinfo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id\r\n',
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '标题\r\n\r\n',
  `visit` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '播放数',
  `barrage` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '弹幕量',
  `up_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'up_id',
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'url',
  `space` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '作者空间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `uk_title`(`title`) USING BTREE,
  INDEX `uk_url`(`url`) USING BTREE,
  INDEX `uk_up`(`up_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 284 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
