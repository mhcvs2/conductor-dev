package config

import "github.com/spf13/viper"

type conductorConfig struct {
	ServerUrl string
	ThreadCount int
}

type dbConfig struct {
	Connection string
}

func NewConductorConfig(serverUrl string, threadCount int) *conductorConfig {
	return &conductorConfig{
		ServerUrl: serverUrl,
		ThreadCount: threadCount,
	}
}

func NewDbConfig(connection string) *dbConfig {
	return &dbConfig{
		Connection: connection,
	}
}

var (
	ConductorConfig *conductorConfig
	DBConfig *dbConfig
)

func Init() {
	viper.SetDefault("conductor.server-url", "http://tx2:8080/api")
	viper.SetDefault("conductor.thread-count", 1)
	viper.SetDefault("database.connection", "root:123@tcp(ali:3306)/db_test?charset=utf8")
	viper.SetEnvPrefix("go_worker")
	viper.BindEnv("conductor.server-url", "conductor.thread-count", "database.connection")

	ConductorConfig = NewConductorConfig(
		viper.GetString("conductor.server-url"),
		viper.GetInt("conductor.thread-count"))
	DBConfig = NewDbConfig(viper.GetString("database.connection"))
}
