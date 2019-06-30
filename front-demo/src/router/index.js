import App from '../App'

const chart1 = r => require.ensure([], () => r(require('@/pages/chart1/index.vue')), 'chart1')
const chart2 = r => require.ensure([], () => r(require('@/pages/chart2/index.vue')), 'chart2')

export default [{
    path: '/',
    component: App,
    children: [ 
        {
            path: '',
            redirect: '/chart1'
        },
        {
            path: '/chart1',
            component: chart1
        },
        {
            path: '/chart2',
            component: chart2
        },
    ]
}]