import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import EditorPage from '../views/EditorPage.vue'
import FinalPage from '../views/FinalPage.vue'

const routes = [
{ path: '/', name: 'Home', component: HomePage },
{ path: '/editor', name: 'Editor', component: EditorPage },
{ path: '/download', name: 'Final', component: FinalPage }
]

const router = createRouter({history: createWebHistory(), routes})

export default router