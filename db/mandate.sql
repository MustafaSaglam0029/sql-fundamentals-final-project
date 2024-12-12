create type mandate_status_types_enum as enum ('Y', 'N', 'R');
create type collection_frequency_types_enum as enum ('D', 'I', 'W', 'M');

create table mandate
(
   business_partner_id   varchar(25) ,
   mandate_status        mandate_status_types_enum ,
   collection_frequency  collection_frequency_types_enum,
   brand                 text  null,
   row_update_datetime   timestamp  null,
   row_create_datetime   timestamp  null,
   changed_by            text null,
   mandate_id            varchar(10) ,
   collection_type       varchar (5)  null,
   metering_consent      varchar(50)  null
);