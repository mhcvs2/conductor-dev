package model

type User struct {
	Id int `orm:"auto"`
	Name string `orm:"size(100)"`
	Age  int
}