package main
 
import (
    "github.com/codegangsta/martini"
    "github.com/codegangsta/martini-contrib/render"
)
 
func main() {
    m := martini.Classic()
 
    // render html template from templates directory
    m.Use(render.Renderer(render.Options{
        Directory:  "templates",
        Layout:     "layout",
        Extensions: []string{".tmpl", ".html"},
        Charset:    "UTF-8",
    }))
 
    m.Get("/", hello)
 
    m.Run()
}
 
func hello(r render.Render) {
    r.HTML(200, "hello", "master")
}
