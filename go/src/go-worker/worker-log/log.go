package worker_log

import "github.com/sirupsen/logrus"

var loggers map[string]logrus.Entry = make(map[string]logrus.Entry)

func init() {
	logrus.SetFormatter(&logrus.TextFormatter{
		DisableColors: true,
		FullTimestamp: true,
	})
	logrus.SetReportCaller(true)
}

func GetLogger(name string) logrus.Entry {
	if entry, ok := loggers[name]; !ok{
		entry = *logrus.WithFields(logrus.Fields{"name": name})
		loggers[name] = entry
		return entry
	} else {
		return entry
	}
}