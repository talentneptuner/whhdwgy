// pages/apartment/apartment.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    list: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: 'http://localhost:8000/getparts/',
      method: 'GET',
      header: {
        'content-type': 'application/json'
      },
      success: function(res){
        console.log(res.data)
        that.setData({
          list : res.data
        })

      }
    })
  },

})