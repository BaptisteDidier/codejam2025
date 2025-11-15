import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import HistoryPage from '../views/HistoryPage.vue'
import InsightsPage from '../views/InsightsPage.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/history', name: 'History', component: HistoryPage },
  { path: '/insights', name: 'Insights', component: InsightsPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
