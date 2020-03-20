var app = new Vue({
  el: '#app',
  // Storing the state of the page
  data: {
    connected: false,
    ros: null,
    ws_address: 'ws://10.0.0.50:9090',
    logs: [],
    loading: false,
    topic: null,
    message: null,
  },

  // Helper methods to connect to ROS
  methods: {
    connect: function() {
      this.loading = true
      //console.log('Connect to rosbridge server!')
      //this.logs.unshift((new Date()).toTimeString() + ' - Connect to rosbridge server!')
      this.ros = new ROSLIB.Ros({
        url: this.ws_address
      })
      this.ros.on('connection', () => {
        //console.log('Connected!')
        this.logs.unshift((new Date()).toTimeString() + ' - Connected!')
        this.connected = true
        this.loading = false
      })
      this.ros.on('error', (error) => {
        //console.log('Error connecting to websocket server: ', error)
        this.logs.unshift((new Date()).toTimeString() + ' - Error connecting to websocket server: $(error)')
      })
      this.ros.on('close', () => {
        //console.log('Connection to websocket server closed!')
        this.logs.unshift((new Date()).toTimeString() + ' - Disconnected!')
        this.connected = false
        this.loading = false
      })
    },

    disconnect: function() {
      //this.logs.unshift((new Date()).toTimeString() + ' - Disconnected!')
      this.ros.close()
      //console.log('Disconnected!')
    },

    setTopic: function() {
      this.topic = new ROSLIB.Topic({
        ros: this.ros,
        name: '/mobile_base/commands/velocity',
        messageType: 'geometry_msgs/Twist'
      })
    },

    forward: function() {
      this.message = new ROSLIB.Message({
        linear: {
          x: 0,
          y: 0,
          z: 0,
        },
        angular: {
          x: 0,
          y: 0,
          z: 0,
        },
      })
      this.setTopic()
      this.topic.publish(this.message)
    },

    stop: function() {
      this.message = new ROSLIB.Message({
        linear: {
          x: 0,
          y: 0,
          z: 0,
        },
        angular: {
          x: 0,
          y: 0,
          z: 0,
        },
      })
      this.setTopic()
      this.topic.publish(this.message)
    },

    backward: function() {
      this.message = new ROSLIB.Message({
        linear: {
          x: 0,
          y: 0,
          z: 0,
        },
        angular: {
          x: 0,
          y: 0,
          z: 0,
        },
      })
      this.setTopic()
      this.topic.publish(this.message)
    },

    turnLeft: function() {
      this.message = new ROSLIB.Message({
        linear: {
          x: 0,
          y: 0,
          z: 0,
        },
        angular: {
          x: 0,
          y: 0,
          z: 0,
        },
      })
      this.setTopic()
      this.topic.publish(this.message)
    },

    turnRight: function() {
      this.message = new ROSLIB.Message({
      linear: {
          x: 0,
          y: 0,
          z: 0,
        },
        angular: {
          x: 0,
          y: 0,
          z: 0,
        },
      })
      this.setTopic()
      this.topic.publish(this.message)
    },
  },
})
