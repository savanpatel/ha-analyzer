create database if not exists ha_analyzer_db;
use ha_analyzer_db;
CREATE TABLE `ha_stats` (
  `date` DATETIME,
  `processnamepid` integer,
  `clientip` char(15),
  `clientport` char(8),
  `accept_date` DATETIME,
  `frontend_listener` text,
  `backend_name` text,
  `server_name` text,
  `Tq` char(5),
  `Tw` char(5),
  `Tc` char(5),
  `Tr` char(5),
  `Tt` char(5),
  `status_code` integer,
  `ac` text,
  `fc` text,
  `bc` text,
  `sc` text,
  `rc` text,
  `srv_queue` text,
  `backend_queue` text,
  `http_request` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
