import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/HomePage'
import AddPage from '@/components/AddPage'


Vue.use(Router)

export default new Router({
    routes:[
        {
            path:'/',
            name: "Home",
            component: HomePage,
            meta: { title: 'Skills - MyApp' }
        },
        {
            path:'/addPage',
            name: "Add",
            component: AddPage,
            meta: { title: 'Skills - MyApp' }
        },

    ]
})