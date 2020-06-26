create database RPS;

use rps;

drop table ショップ情報;

create table ショップ情報
	(id int primary key auto_increment,
		ショップ名 varchar(100) not null,
		送料 varchar(100),
        ５％還元 tinyint,
        ショップURL varchar(1000)
        );


drop database amnshop;

desc ショップ情報;

insert into ショップ情報(ショップ名) values('トレジャービューティー');
insert into ショップ情報(送料) values('12000円以上無料');
insert into ショップ情報(５％還元) values(1);
insert into ショップ情報(ショップURL) values('https://www.rakuten.ne.jp/gold/treasurebeauty/');


insert into ショップ情報(ショップ名) values('トレジャービューティー');
insert into ショップ情報(送料) values('12000円以上無料');
insert into ショップ情報(５％還元) values(1);
insert into ショップ情報(ショップURL) values('https://www.rakuten.ne.jp/gold/treasurebeauty/');
truncate ショップ情報;

insert into ショップ情報　values(1,
'トレジャービューティー',
'12000円以上無料',
'1',
'https://www.rakuten.ne.jp/gold/treasurebeauty/'
);
    
select *from ショップ情報;
    