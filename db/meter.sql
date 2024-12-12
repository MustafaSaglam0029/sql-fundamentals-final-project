create type smart_collectable_types_enum as enum ('0', '1');

create table meter
(
  business_partner_id  varchar(25) ,
  connection_ean_code  varchar(50) ,
  grid_company_code    varchar(25),
  oda_code             varchar(25),
  meter_number         varchar(25) ,
  smart_collectable    smart_collectable_types_enum,
  brand                varchar(25)   null,
  sjv1                 varchar(25)  null,
  sjv2                 varchar(25)  null,
  installation         varchar(25)  null,
  division             varchar(25)  null,
  move_out_date        timestamp null,
  row_create_datetime  timestamp  null,
  move_in_date         timestamp  null
);


