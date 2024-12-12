create type mandate_status_types_enum as enum ('Y', 'N', 'R');
create type collection_frequency_types_enum as enum ('D', 'I', 'W', 'M');

create table mandate
(
   business_partner_id   varchar(25) unique,
   mandate_status        mandate_status_types_enum ,
   collection_frequency  collection_frequency_types_enum,
   brand                 text not null,
   row_update_datetime   timestamp not null,
   row_create_datetime   timestamp not null,
   changed_by            text null,
   mandate_id            varchar(10) primary key,
   collection_type       varchar (5) not null,
   metering_consent      varchar(50) not null
);