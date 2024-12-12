create type energy_types_enum as enum ('GAS', 'ELECTRICITY');


create table meter_readings
(
   account_id           varchar(25) primary key,
   brand                varchar(25) not null,
   connection_ean_code  varchar(50),
   energy_type          energy_types_enum,
   meter_number         varchar (25) unique,
   reading_date         date   not null,
   reading_electricity  varchar(250) null,
   reading_gas          varchar(250) null,
   rejection            varchar(250) null,
   validation_status    varchar(25)  null,
   constraint fk_connection_ean_code
              foreign key(connection_ean_code) references meter(connection_ean_code)
);
