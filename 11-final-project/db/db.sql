CREATE TABLE `chess`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `user_games` INT NULL,
  `user_wins` INT NULL,
  `user_losses` INT NULL,
  `user_saved_game_id` INT NULL,
  `user_current_game_id` INT NULL,
  PRIMARY KEY (`user_id`));

CREATE TABLE `chess`.`game` (
  `game_id` INT NOT NULL AUTO_INCREMENT,
  `game_board` TINYTEXT NOT NULL,
  `game_time` INT NOT NULL,
  `game_white_time` INT NOT NULL,
  `game_black_time` INT NOT NULL,
  `game_white_player_id` INT NOT NULL,
  `game_black_player_id` INT NOT NULL,
  PRIMARY KEY (`game_id`));

INSERT INTO user (user_name, user_games, user_wins, user_losses, user_saved_game_id, user_current_game_id) VALUES ('Afghanistan', 0, 0, 0, NULL, NULL);