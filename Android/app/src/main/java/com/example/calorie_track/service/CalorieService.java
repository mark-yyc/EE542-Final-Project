package com.example.calorie_track.service;

import com.example.calorie_track.data.CalorieInfo;

import retrofit2.Call;
import retrofit2.http.GET;

public interface CalorieService {
    @GET("calorie_today")
    Call<CalorieInfo> getCalorieInfo();
}
