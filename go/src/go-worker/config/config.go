package config

import (
	"github.com/sirupsen/logrus"
	"github.com/spf13/viper"
	"strings"
)

type commonConfig struct {
	LogLevel string
}

func (c *commonConfig) getLogLevel() logrus.Level {
	level := strings.ToLower(c.LogLevel)
	switch level {
	case "fatal":
		return logrus.FatalLevel
	case "error":
		return logrus.ErrorLevel
	case "warn":
		return logrus.WarnLevel
	case "debug":
		return logrus.DebugLevel
	default:
		return logrus.InfoLevel
	}
}

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

func NewCommonConfig(logLevel string) *commonConfig {
	return &commonConfig{
		LogLevel: logLevel,
	}
}

var (
	ConductorConfig *conductorConfig
	DBConfig *dbConfig
	CommonConfig * commonConfig
)

func Init() {
	viper.SetDefault("conductor.server-url", "http://ali:8080/api")
	viper.SetDefault("conductor.thread-count", 1)
	viper.SetDefault("database.connection", "root:123@tcp(ali:3306)/db_test?charset=utf8")
	viper.SetDefault("log.level", "info")
	viper.SetEnvPrefix("go_worker")
	viper.BindEnv("conductor.server-url", "conductor.thread-count", "database.connection", "log.level")

	ConductorConfig = NewConductorConfig(
		viper.GetString("conductor.server-url"),
		viper.GetInt("conductor.thread-count"))
	DBConfig = NewDbConfig(viper.GetString("database.connection"))
	CommonConfig = NewCommonConfig(viper.GetString("log.level"))
}
