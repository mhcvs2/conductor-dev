package com.mhc.test.springbootpg.config;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mhc.test.springbootpg.dao.MetadataDAO;
import com.mhc.test.springbootpg.dao.PostgresMetadataDAO;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.boot.autoconfigure.flyway.FlywayConfigurationCustomizer;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.DependsOn;
import org.springframework.context.annotation.Import;

import javax.sql.DataSource;


@SuppressWarnings("SpringJavaInjectionPointsAutowiringInspection")
@Configuration(proxyBeanMethods = false)
//@EnableConfigurationProperties(PostgresProperties.class)
@ConditionalOnProperty(name = "db.type", havingValue = "postgres")
// Import the DataSourceAutoConfiguration when postgres database is selected.
// By default the datasource configuration is excluded in the main module.
@Import(DataSourceAutoConfiguration.class)
public class PGConfiguration {

    @Bean
    public FlywayConfigurationCustomizer flywayConfigurationCustomizer() {
        // override the default location.
        return configuration -> configuration.locations("classpath:db/migration");
    }

    @Bean
    @DependsOn({"flyway", "flywayInitializer"})
    public MetadataDAO postgresMetadataDAO(ObjectMapper objectMapper, DataSource dataSource) {
        return new PostgresMetadataDAO(objectMapper, dataSource);
    }

}
