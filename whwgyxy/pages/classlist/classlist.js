// pages/classlist/classlist.js
var g_list=[]

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
    wx.request({
      url: 'http://localhost:8000/getgrade/',
      method: 'GET',
      header: {
        'content-type': 'application/json'
      },
      success:function(res){
        for (var i in res.data){
          res.data[i].show = false
        }
        g_list = res.data
        that.setData({
          grades : res.data
        })
      }
    })
  },

  showContent: function(res){
    var that = this
    var id = res.currentTarget.dataset.id;
    var aid = id-1;
    g_list[aid].show = g_list[aid].show?false:true;
    // console.log(g_list)
    that.setData({
      grades:g_list
    })
  },
  ToClass: function(res){
    var id = res.currentTarget.dataset.cid;
    wx.navigateTo({
      url: '/pages/class/class?id='+id,
    })
  }
})