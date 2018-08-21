// pages/sightdetail/sightdetail.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    var id = options.id
    wx.request({
      url: 'http://localhost:8000/getsightinfo/'+id,
      method: 'GET',
      header: {
        'Accept': 'application/json'
      },
      success : function(res) {
        console.log(res.data)
        that.setData({
          title: res.data.title,
          imagelist : res.data.imagelist,
          desc: res.data.desc
        })
      }
    })
  
  },

  
})