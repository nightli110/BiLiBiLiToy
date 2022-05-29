/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.1.49
 Source Server Type    : MySQL
 Source Server Version : 50730
 Source Host           : 192.168.1.49:3306
 Source Schema         : bilibilitest

 Target Server Type    : MySQL
 Target Server Version : 50730
 File Encoding         : 65001

 Date: 29/05/2022 21:31:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bilibili_videoimage
-- ----------------------------
DROP TABLE IF EXISTS `bilibili_videoimage`;
CREATE TABLE `bilibili_videoimage`  (
  `videoId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loadStatus` tinyint(1) NULL DEFAULT NULL,
  `path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `uk_videoid`(`videoId`) USING BTREE,
  INDEX `uk_videoid_status`(`videoId`, `loadStatus`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 104 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
