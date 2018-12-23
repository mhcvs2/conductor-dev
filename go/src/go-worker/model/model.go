package model

import (
	"github.com/astaxie/beego/orm"
	_ "github.com/go-sql-driver/mysql"
	"go-worker/config"
)

var (
	DBOrm orm.Ormer
)

func Init() {
	orm.RegisterModel(new(User))
	orm.RegisterDataBase("default", "mysql", config.DBConfig.Connection, 30)
	DBOrm = orm.NewOrm()
}
