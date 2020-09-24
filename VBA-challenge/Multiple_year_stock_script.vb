
Sub loopStock():



''declare variables
Dim ws As Worksheet


''add headers for each sheet
For Each ws In ThisWorkbook.Worksheets
    ws.Cells(1, 10) = "Ticker"
    ws.Cells(1, 11) = "Yearly Change"
    ws.Cells(1, 12) = "Percentage Change"
    ws.Cells(1, 13) = "Total Stock Volume"
    
    ws.Cells(1, 17) = "Ticker"
    ws.Cells(1, 18) = "Value"
    ws.Cells(2, 16) = "Greatest % increase"
    ws.Cells(3, 16) = "Greatest % decrease"
    ws.Cells(4, 16) = "Greatest total volume"
    
''declare variables
Dim rng As Range
Dim ticker As String
Dim totVolume As Double
Dim yrChange As Double
Dim perChange As Double
Dim stockBegPrice As Double
Dim stockEndPrice As Double
Dim lstrow As Long
Dim rwTicker As Long
Dim maxTicker As String
Dim minTicker As String
Dim maxPercIncr As Double
Dim minPercIncr As Double
Dim maxTotVolume As Long
Dim maxTotVolTicker As String



'get last row
Set rng = Range("A1", Range("A1").End(xlDown))
lstrow = rng.Count

'start row
rwTicker = 2
stockBegPrice = ws.Cells(2, 3).Value
totVolume = 0
yrChange = 0
maxPercIncr = 0
minPercIncr = 0
maxTotVolume = 0


  ''loop through the rows
  
    For i = 2 To lstrow:
    
      
       If (ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value) Then
       
            'ticker column
            ticker = ws.Cells(i, 1).Value
            
            
            'total volume column
            totVolume = totVolume + ws.Cells(i, 7).Value
            
            
            stockEndPrice = ws.Cells(i, 6).Value
            yrChange = (stockEndPrice - stockBegPrice)
            
            
            If stockBegPrice <> 0 Then
            yrChangePerc = (yrChange / stockBegPrice) * 100
            
            End If
            
            
              
          '' Greatest% increase and decrease ticker and value
            If yrChangePerc > maxPercIncr Then
                    maxTicker = ticker
                    maxPercIncr = yrChangePerc
            
            ElseIf yrChangePerc < minPercIncr Then
                    minTicker = ticker
                    minPercIncr = yrChangePerc
            End If
            
            
            
                
          'create the new columns rollup by ticker and values
         
            ws.Range("J" & rwTicker).Value = ticker
            ws.Range("K" & rwTicker).Value = yrChange
            ws.Range("L" & rwTicker).Value = CStr(yrChangePerc) + "%"
            ws.Range("M" & rwTicker).Value = totVolume
            
            ws.Range("Q2").Value = maxTicker
            ws.Range("Q3").Value = minTicker
            ws.Range("R2").Value = CStr(maxPercIncr) + "%"
            ws.Range("R3").Value = CStr(minPercIncr) + "%"
            
                               
           ''Greatest total volume ticker and value
              If totVolume > maxTotVolume Then
                maxTotVolTicker = ticker
                maxtotVol = totVolume
                
                ws.Range("Q4").Value = maxTotVolTicker
                ws.Range("R4").Value = maxtotVol
         
         
          
          'reset ticker rows
          
            rwTicker = rwTicker + 1
            stockEndPrice = 0
            stockBegPrice = ws.Cells(i + 1, 3).Value
            yrChange = 0
            totVolume = 0
         
            
        Else
           totVolume = totVolume + ws.Cells(i, 7).Value
 
            
              End If
               
            
        End If
            
    Next
    
    ''conditional formatting that will highlight positive change in green and negative change in red.

    Set rng = Range("K1", Range("K1").End(xlDown))
    lstrowChg = rng.Count

    
        For i = 2 To lstrowChg:
    
            If ws.Cells(i, 11).Value < 0 Then
                'red for negatve
                ws.Cells(i, 11).Interior.ColorIndex = 3
                Else
            
                'green for postive
                ws.Cells(i, 11).Interior.ColorIndex = 4
             End If
            
      
   
            
        Next
        
  
Next ws
    
    
    
    MsgBox ("Code Completed")
    
End Sub


Sub delColumns():
Dim ws As Worksheet

For Each ws In ThisWorkbook.Worksheets
    ws.Range("i1:R1000000").Delete
    
Next
MsgBox ("Columns Deleted")
End Sub


