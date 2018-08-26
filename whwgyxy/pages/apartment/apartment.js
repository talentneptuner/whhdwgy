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

  ToTeachers : function(res){
    var id = res.currentTarget.dataset.id;
    wx.request({
      url: 'http://localhost:8000/getteachers/'+id,
      method: 'GET',
      header: {
        'Accept': 'application/json'
      },
      success : function(data){
        data = data.data
        if (!data.click){
          wx.showToast({
            title: '数据暂未添加，请期待哦',
            icon:'none',
          })
          return
        }
        wx.navigateTo({
          url: '/pages/teachers/teachers?id='+data.id,
        })
      }
    })
  }

})